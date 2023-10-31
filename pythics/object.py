from .vector import Vector
from .physics import Physics
from .colliders import Collider

class Object:

    globalGravity = Vector(0, 100)

    def __init__(self, position: Vector = Vector(0, 0), mass: int = 1, velocity: Vector = Vector(0, 0), acceleration: Vector = Vector(0, 0), gravity = True):
        self.position: Vector = position
        self.mass: int = mass
        self.velocity: Vector = velocity
        self.acceleration: Vector = acceleration
        self.total_force = Vector(0, 0)
        
        if gravity:
            self.addForce(Object.globalGravity)

        Physics.instance.objects.add(self)

    def addVelocity(self, velocity: Vector):
        self.velocity += velocity

    def addForce(self, force: Vector):
        self.total_force += force

    def addGravity(self):
        self.addForce(Object.globalGravity)

    def update(self, dt):
        self.velocity += (self.acceleration * dt) + (self.total_force * dt)

        self.position += self.velocity * dt


class CollidableObject(Object):
    def __init__(self, position: Vector = Vector(0, 0), mass: int = 1, velocity: Vector = Vector(0, 0), acceleration: Vector = Vector(0, 0), gravity = True, collider: Collider = Collider):
        super().__init__(position = Vector(0, 0), mass = 1, velocity = Vector(0, 0), acceleration = Vector(0, 0), gravity = True)
        self.collider = collider

        self.lastMovement = Vector(0, 0)

    def update(self, dt):
        self.velocity += (self.acceleration * dt) + (self.total_force * dt)

        self.lastMovement = self.velocity * dt

        self.position += self.velocity * dt

        self.collider.collide()
