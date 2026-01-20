import { Vec2 } from './Vec2.js';

export class Transform {
    constructor(x = 0, y = 0, angle = 0) {
        this.pos = new Vec2(x, y);
        this.angle = angle;
    }
}