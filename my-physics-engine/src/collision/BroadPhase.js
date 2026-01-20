export class BroadPhase {
    // Basic AABB check implementation
    static getPotentialPairs(bodies) {
        let pairs = [];
        for (let i = 0; i < bodies.length; i++) {
            for (let j = i + 1; j < bodies.length; j++) {
                // TODO: Add AABB check here
                pairs.push([bodies[i], bodies[j]]);
            }
        }
        return pairs;
    }
}