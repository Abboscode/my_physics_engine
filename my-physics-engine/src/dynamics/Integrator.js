export class Integrator {
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
}