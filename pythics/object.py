from pythics.vector import Vector

class Object:
    def __init__(self, position: Vector = Vector(0, 0), mass: int = 1, velocity: Vector = Vector(0, 0), acceleration: Vector = Vector(0, 0)):
        self.position: Vector = position
        self.mass: int = mass
        self.velocity: Vector = velocity
        self.acceleration: Vector = acceleration
        self.total_force = Vector(0, 0)

    def addVelocity(self, velocity: Vector):
        self.velocity += velocity

    def applyForce(self, force: Vector):
        self.total_force += force

    def removeForce(self, force: Vector):
        self.total_force -= force

    def update(self, dt):
        self.velocity += (self.acceleration * dt) + (self.total_force * dt)

        self.position += self.velocity * dt