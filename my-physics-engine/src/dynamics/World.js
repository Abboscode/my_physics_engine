import { Vec2 } from '../math/Vec2.js';
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
}