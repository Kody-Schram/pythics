from vector import Vector

class Object:
    def __init__(self, position: Vector = Vector(0, 0), mass: int = 100, velocity: Vector = Vector(0, 0), acceleration: Vector = Vector(0, -9.8)):
        self.position: Vector = position
        self.mass: int = mass
        self.velocity: Vector = velocity
        self.acceleration: Vector = acceleration

    def applyForce(self, newtons):
        appliedAcceleration = newtons / self.mass
        self.acceleration += appliedAcceleration

    def update(self, dt):
        self.velocity += self.acceleration * dt

        self.position += self.velocity * dt