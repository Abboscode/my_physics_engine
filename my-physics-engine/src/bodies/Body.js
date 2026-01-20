import { Vec2 } from '../math/Vec2.js';
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
}