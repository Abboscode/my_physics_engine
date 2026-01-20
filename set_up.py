import os

# Define the root directory name
ROOT_DIR = "my-physics-engine"

# Define the file structure and initial content
project_structure = {
    # ---------------------------------------------------------
    # ROOT FILES
    # ---------------------------------------------------------
    "package.json": """{
  "name": "my-physics-engine",
  "version": "1.0.0",
  "description": "A physics engine from scratch in JS",
  "main": "index.html",
  "scripts": {
    "test": "echo \\"Error: no test specified\\" && exit 1"
  },
  "author": "",
  "license": "ISC"
}""",

    "index.html": """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Physics Engine Demo</title>
    <style>
        body { margin: 0; overflow: hidden; background: #222; }
        canvas { display: block; }
    </style>
</head>
<body>
    <canvas id="simCanvas"></canvas>
    <script type="module" src="./src/main.js"></script>
</body>
</html>""",

    # ---------------------------------------------------------
    # MATH LIBRARY
    # ---------------------------------------------------------
    "src/math/Vec2.js": """export class Vec2 {
    constructor(x = 0, y = 0) {
        this.x = x;
        this.y = y;
    }

    add(v) { this.x += v.x; this.y += v.y; return this; }
    sub(v) { this.x -= v.x; this.y -= v.y; return this; }
    scale(n) { this.x *= n; this.y *= n; return this; }
    
    dot(v) { return this.x * v.x + this.y * v.y; }
    cross(v) { return this.x * v.y - this.y * v.x; }
    
    mag() { return Math.sqrt(this.x * this.x + this.y * this.y); }
    normalize() {
        const m = this.mag();
        if (m > 0) this.scale(1 / m);
        return this;
    }

    static copy(v) { return new Vec2(v.x, v.y); }
}""",

    "src/math/Mat2.js": """export class Mat2 {
    constructor(a = 1, b = 0, c = 0, d = 1) {
        this.a = a; this.b = b; // Col 1
        this.c = c; this.d = d; // Col 2
    }

    setRotation(radians) {
        const c = Math.cos(radians);
        const s = Math.sin(radians);
        this.a = c; this.c = -s;
        this.b = s; this.d = c;
    }
}""",

    "src/math/Utils.js": """export const clamp = (min, max, val) => Math.max(min, Math.min(val, max));
export const EPSILON = 0.0001;""",

    "src/math/Transform.js": """import { Vec2 } from './Vec2.js';

export class Transform {
    constructor(x = 0, y = 0, angle = 0) {
        this.pos = new Vec2(x, y);
        this.angle = angle;
    }
}""",

    # ---------------------------------------------------------
    # SHAPES
    # ---------------------------------------------------------
    "src/shapes/Shape.js": """export class Shape {
    constructor(type) {
        this.type = type; // 'Circle', 'Box', etc.
    }
    
    computeInertia(mass) {
        throw new Error("computeInertia not implemented");
    }
}""",

    "src/shapes/Circle.js": """import { Shape } from './Shape.js';

export class Circle extends Shape {
    constructor(radius) {
        super('Circle');
        this.radius = radius;
    }

    computeInertia(mass) {
        return mass * this.radius * this.radius * 0.5;
    }
}""",

    "src/shapes/Box.js": """import { Shape } from './Shape.js';

export class Box extends Shape {
    constructor(width, height) {
        super('Box');
        this.width = width;
        this.height = height;
    }

    computeInertia(mass) {
        return mass * (this.width * this.width + this.height * this.height) / 12;
    }
}""",

    # ---------------------------------------------------------
    # BODIES
    # ---------------------------------------------------------
    "src/bodies/Body.js": """import { Vec2 } from '../math/Vec2.js';
import { Transform } from '../math/Transform.js';

export class Body {
    constructor(shape, x, y) {
        this.shape = shape;
        this.transform = new Transform(x, y);
        this.linearVelocity = new Vec2(0, 0);
        this.angularVelocity = 0;
        this.force = new Vec2(0, 0);
        this.torque = 0;
        
        this.mass = 0;
        this.invMass = 0;
        this.inertia = 0;
        this.invInertia = 0;
        
        this.restitution = 0.5; // Bounciness
        this.friction = 0.5;
    }

    setMass(m) {
        if (m === 0) {
            this.mass = 0;
            this.invMass = 0;
            this.inertia = 0;
            this.invInertia = 0;
        } else {
            this.mass = m;
            this.invMass = 1 / m;
            this.inertia = this.shape.computeInertia(m);
            this.invInertia = 1 / this.inertia;
        }
    }
}""",

    # ---------------------------------------------------------
    # COLLISION
    # ---------------------------------------------------------
    "src/collision/Manifold.js": """export class Manifold {
    constructor(bodyA, bodyB) {
        this.bodyA = bodyA;
        this.bodyB = bodyB;
        this.penetration = 0;
        this.normal = null; // Vec2
        this.contacts = []; // Array of Vec2
    }
}""",

    "src/collision/BroadPhase.js": """export class BroadPhase {
    // Basic AABB check implementation
    static getPotentialPairs(bodies) {
        let pairs = [];
        for (let i = 0; i < bodies.length; i++) {
            for (let j = i + 1; j < bodies.length; j++) {
                // TODO: Add AABB check here
                pairs.push([bodies[i], bodies[j]]);
            }
        }
        return pairs;
    }
}""",

    "src/collision/NarrowPhase.js": """import { Manifold } from './Manifold.js';

export class NarrowPhase {
    static detect(bodyA, bodyB) {
        // TODO: Implement SAT (Separating Axis Theorem)
        return null; // Return new Manifold if collision detected
    }
}""",

    # ---------------------------------------------------------
    # DYNAMICS & SOLVERS
    # ---------------------------------------------------------
    "src/dynamics/Integrator.js": """export class Integrator {
    static integrate(body, dt, gravity) {
        if (body.invMass === 0) return;

        // Apply Forces
        const accel = new Vec2(body.force.x * body.invMass, body.force.y * body.invMass);
        accel.add(gravity);

        // Update Velocity
        body.linearVelocity.x += accel.x * dt;
        body.linearVelocity.y += accel.y * dt;

        // Update Position
        body.transform.pos.x += body.linearVelocity.x * dt;
        body.transform.pos.y += body.linearVelocity.y * dt;

        // Clear forces
        body.force.x = 0;
        body.force.y = 0;
    }
}""",

    "src/dynamics/Solver.js": """export class Solver {
    static resolve(manifold) {
        // TODO: Apply impulses to separate bodies
    }
}""",

    "src/dynamics/World.js": """import { Vec2 } from '../math/Vec2.js';
import { Integrator } from './Integrator.js';
import { BroadPhase } from '../collision/BroadPhase.js';

export class World {
    constructor() {
        this.bodies = [];
        this.gravity = new Vec2(0, 9.81);
    }

    addBody(body) {
        this.bodies.push(body);
    }

    step(dt) {
        // 1. Broadphase
        // 2. Narrowphase
        // 3. Solve Constraints
        // 4. Integrate
        for (let body of this.bodies) {
            Integrator.integrate(body, dt, this.gravity);
        }
    }
}""",

    # ---------------------------------------------------------
    # MAIN ENTRY
    # ---------------------------------------------------------
    "src/main.js": """import { World } from './dynamics/World.js';
import { Body } from './bodies/Body.js';
import { Circle } from './shapes/Circle.js';

const canvas = document.getElementById('simCanvas');
const ctx = canvas.getContext('2d');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

const world = new World();

// Add a test ball
const ball = new Body(new Circle(20), canvas.width / 2, 100);
ball.setMass(10);
world.addBody(ball);

function loop() {
    // Clear screen
    ctx.fillStyle = '#222';
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Update Physics
    world.step(1/60);

    // Render
    ctx.fillStyle = '#fff';
    for (let body of world.bodies) {
        ctx.beginPath();
        ctx.arc(body.transform.pos.x, body.transform.pos.y, body.shape.radius, 0, Math.PI * 2);
        ctx.fill();
    }

    requestAnimationFrame(loop);
}

loop();"""
}

def create_project():
    print(f"🚀 Initializing project at: {os.path.abspath(ROOT_DIR)}")
    
    if not os.path.exists(ROOT_DIR):
        os.makedirs(ROOT_DIR)

    for file_path, content in project_structure.items():
        # Construct full path
        full_path = os.path.join(ROOT_DIR, file_path)
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(full_path), exist_ok=True)
        
        # Write file
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content)
            
        print(f"   Created: {file_path}")

    print("\n✅ Project structure created successfully!")
    print(f"👉 Go to the folder: cd {ROOT_DIR}")
    print("👉 Open 'index.html' in your browser (or serve it via a local server).")

if __name__ == "__main__":
    create_project()