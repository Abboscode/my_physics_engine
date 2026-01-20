export class Shape {
    constructor(type) {
        this.type = type; // 'Circle', 'Box', etc.
    }
    
    computeInertia(mass) {
        throw new Error("computeInertia not implemented");
    }
}