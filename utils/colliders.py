from .vector import Vector
from .funcs import clamp
import math

class BoxCollider:
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    @property
    def position(self) -> Vector:
        return Vector(self.x, self.y)

    @property
    def as_tup(self):
        return (self.position.x, self.position.y, self.width, self.height)


    def collide_point(self, point: Vector) -> bool:
        return (self.x <= point.x and self.x + self.width >= point.x) and (self.y <= point.y and self.y + self.height >= point.y)

    def collide_rect(self, rect):
        collide = False

        if (self.x <= rect.x + rect.width and self.x + self.width >= rect.x) and (self.y <= rect.y + rect.height and self.y + self.height >= rect.y):
            collide = True

    
class CircleCollider:
    def __init__(self, x, y, radius) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def position(self) -> Vector:
        return Vector(self.x, self.y)

    
    @property
    def as_tup(self):
        return (self.x, self.y, self.width, self.height)

    # Returns bool for hit and rebound off point
    def collide_point(self, point: Vector):
        distance = self.position.sub(point)

        angle = math.atan2(distance.y, distance.x)
        x = math.cos(angle) * self.radius
        y = math.sin(angle) * self.radius
        closest = Vector(self.position.x - x, self.position.y - y)

        return (distance.magnitude <= self.radius, point.sub(closest), closest)

    # Returns bool for a collision and a Vector for the rebound if there was a hit
    def collide_circle(self, other: 'CircleCollider'):
        distance = other.position.sub(self.position)
        collide = False

        if distance.magnitude - other.radius <= self.radius:
            collide = True

        angle = math.atan2(distance.y, distance.x)
        x = math.cos(angle) * self.radius
        y = math.sin(angle) * self.radius
        p1 = Vector(self.position.x - x, self.position.y - y)

        distance = self.position.sub(other.position)
        angle = math.atan2(distance.y, distance.x)
        x = math.cos(angle) * other.radius
        y = math.sin(angle) * other.radius
        p2 = Vector(other.position.x - x, other.position.y - y)

        return (collide, p2.sub(p1))


    def collide_rect(self, other: BoxCollider):
        closest = Vector(clamp(self.position.x, other.x, other.x + other.width), clamp(self.position.y, other.y, other.y + other.y))
        collide = self.collide_point(closest)[0]

        direction = closest.sub(self.position)
        angle = math.atan2(direction.y, direction.x)
        x = math.cos(angle) * self.radius
        y = math.sin(angle) * self.radius

        p = Vector(self.x - x, self.y - y)

        return (collide, closest.sub(p))
