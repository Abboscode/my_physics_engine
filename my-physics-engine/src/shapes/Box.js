import { Shape } from './Shape.js';

export class Box extends Shape {
    constructor(width, height) {
        super('Box');
        this.width = width;
        this.height = height;
    }

    computeInertia(mass) {
        return mass * (this.width * this.width + this.height * this.height) / 12;
    }
}