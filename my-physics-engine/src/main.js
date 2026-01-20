// import { World } from './dynamics/World.js';
// import { Body } from './bodies/Body.js';
// import { Circle } from './shapes/Circle.js';





// const canvas = document.getElementById('simCanvas');
// const ctx = canvas.getContext('2d');
// canvas.width = window.innerWidth;
// canvas.height = window.innerHeight;

// const world = new World();

// Add a test ball
// const ball = new Body(new Circle(20), canvas.width / 2, 100);
// ball.setMass(10);
// world.addBody(ball);


const canvas = document.getElementById('simCanvas');
const ctx = canvas.getContext('2d');

class Vec4 {
    constructor(x = 0, y = 0, z = 0, w = 1) {
        this.x = x;
        this.y = y;
        this.z = z;
        this.w = w;
    }
}
class Mat4 {
    static identity() {
        return new Float32Array(16).fill(0).map((v, i) => (i % 5 === 0 ? 1 : 0));
    }
    static projection(width, height, depth, fov = 60) {
        const aspect = width / height;
        const fovRad = 1 / Math.tan((fov * 0.5) * (Math.PI / 180));
        const lambda = zfar / (zfar - znear);
        return new Float32Array([
            aspect * fovRad, 0, 0, 0,
            0, fovRad, 0, 0,
            0, 0, lambda, -lambda * znear,
            0, 0, 1, 0
        ]);
    }
}
const v = 50;
let z = 2;

function projection(vector,tovector){

let result = new Vec4();

let det = tovector[0]**2+tovector[1]**2+tovector[2]**2;
   for (let i = 0; i < vector.length; i++) {
        result.x += vector[i] * tovector[i];
    result.y += vector[i + 4] * tovector[i + 4];
    result.z += vector[i + 8] * tovector[i + 8];


}

result.x = result.x / det;
result.y = result.y / det;
result.z = result.z / det;

return result;
}



let vxf=new Vec4(v, 1, 1);
let vyf=new Vec4(1, v, 1);
let vzf=new Vec4(v, v, 1);
const triangle = {



    //fromt
    verticesFront: [new Vec4(1, 1, 1), vxf, vyf, vzf],
    //back
    verticesBack: [new Vec4(1, 1, 1), projection(new (v,1,1))new Vec4(v, 1, 1), new Vec4(1*z, v*z, 1), new Vec4(v*z, v*z, 1)],
    tringles: [[0, 1, 2, 0], [1, 2, 3, 1]]


}
const offsetX = canvas.width / 2 - v / 2;
const offsetY = canvas.height / 2 - v / 2;

function loop() {
    // Clear screen
    ctx.fillStyle = '#e7e0e0';

    ctx.beginPath();

    ctx.fillRect(0, 0, canvas.width, canvas.height);
    ctx.strokeStyle = '#000000';
    ctx.lineWidth = 2;

    for (let tri of triangle.tringles) {
        const firstPoint = triangle.verticesFront[tri[0]];
        ctx.moveTo(firstPoint.x + offsetX, firstPoint.y + offsetY);

        for (let index = 1; index < tri.length; index++) {


            const p = triangle.verticesFront[tri[index]];
            ctx.lineTo(p.x + offsetX, p.y + offsetY);
        }
         ctx.moveTo((firstPoint.x )+ offsetX, (firstPoint.y )+ offsetY);
        for (let index = 1; index < tri.length; index++) {



            const p = triangle.verticesBack[tri[index]];
            ctx.lineTo((p.x) + offsetX , (p.y) + offsetY);
        }





    }
    ctx.closePath();
    ctx.stroke();


    // Draw Triangle


    // Update Physics



    requestAnimationFrame(loop);
}

loop();