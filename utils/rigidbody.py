from .vector import Vector
from .physics import deltaTime

class RigidBody:
    def __init__(self, x, y, gravity, drag, velocity) -> None:
        self.x, self.y = x, y
        self.gravity = gravity
        self.drag = drag
        self.velocity = velocity

    
    def simulate(self) -> None:
        self.x += self.velocity.x * deltaTime
        self.y += self.velocity.y * deltaTime

        self.velocity.y += self.gravity