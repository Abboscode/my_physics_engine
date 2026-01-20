export class Manifold {
    constructor(bodyA, bodyB) {
        this.bodyA = bodyA;
        this.bodyB = bodyB;
        this.penetration = 0;
        this.normal = null; // Vec2
        this.contacts = []; // Array of Vec2
    }
}