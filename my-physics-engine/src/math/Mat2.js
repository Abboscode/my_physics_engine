export class Mat2 {
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
}