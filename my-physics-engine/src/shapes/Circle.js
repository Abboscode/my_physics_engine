import { Shape } from './Shape.js';

export class Circle extends Shape {
    constructor(radius) {
        super('Circle');
        this.radius = radius;
    }

    computeInertia(mass) {
        return mass * this.radius * this.radius * 0.5;
    }
}