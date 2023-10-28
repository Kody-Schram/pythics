from .vector import Vector

class Object:
    def __init__(self, position: Vector = Vector(0, 0), mass: int = 1, velocity: Vector = Vector(0, 0), acceleration: Vector = Vector(0, 0), normalForce: bool = False):
        self.position: Vector = position
        self.mass: int = mass
        self.velocity: Vector = velocity
        self.acceleration: Vector = acceleration
        self.normalForce = normalForce

    def addVelocity(self, velocity: Vector):
        self.velocity += velocity

    def update(self, dt):
        if not self.normalForce:
            self.velocity += (self.acceleration * dt) + (Vector(0, 100) * dt)
        else:
            self.velocity += (self.acceleration * dt)

        print(f'velocity {self.velocity}')

        self.position += self.velocity * dt