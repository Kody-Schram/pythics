from typing import overload
from pythics.utils.vector import Vector
from pythics.utils.funcs import clamp
import math

# Basic rect or square collider
class BoxCollider:
    def __init__(self, x, y, width, height) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    # Quality of life functions
    @property
    def position(self) -> Vector:
        return Vector(self.x, self.y)

    @property
    def as_tup(self):
        return (self.position.x, self.position.y, self.width, self.height)


    # Collision detection functions
    def collide_point(self, point: Vector) -> bool:
        """Returns -> (bool, Vector)
           Bool value is whether or not they collide
           Vector returned is the displacement vector
           
           Determines if the current object(BoxCollider) collides with a point(Vector)"""
        return (self.x <= point.x and self.x + self.width >= point.x) and (self.y <= point.y and self.y + self.height >= point.y)

    def collide_rect(self, rect):
        """Returns -> (bool, Vector)
           Bool value is whether or not they collide
           Vector returned is the displacement vector
           
           Determines if the current object(BoxCollider) collides with a given collider(BoxCollider)"""
        collide = False

        if (self.x <= rect.x + rect.width and self.x + self.width >= rect.x) and (self.y <= rect.y + rect.height and self.y + self.height >= rect.y):
            collide = True

    
class CircleCollider:
    def __init__(self, x, y, radius) -> None:
        self.x = x
        self.y = y
        self.radius = radius

    # Quality of life functions
    @property
    def position(self) -> Vector:
        return Vector(self.x, self.y)
    
    @property
    def as_tup(self):
        return (self.x, self.y, self.width, self.height)


    # Collision detection functions
    def collide_point(self, point: Vector):
        """Returns -> (bool, Vector)
           Bool value is whether or not they collide
           Vector returned is the displacement Vector
           
           Determines if the current object(CircleCollider) collides with the given point(Vector)"""

        distance = self.position - point

        angle = math.atan2(distance.y, distance.x)
        x = math.cos(angle) * self.radius
        y = math.sin(angle) * self.radius
        closest = Vector(self.position.x - x, self.position.y - y)

        return (distance.magnitude <= self.radius, point - closest)

    # Returns bool for a collision and a Vector for the rebound if there was a hit
    def collide_circle(self, other: 'CircleCollider'):
        distance = other.position - self.position
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

        return (collide, p2 - p1)


    def collide_rect(self, other: BoxCollider):
        closest = Vector(clamp(self.position.x, other.x, other.x + other.width), clamp(self.position.y, other.y, other.y + other.y))
        collide = False

        distance = closest - self.position
        if distance.magnitude <= self.radius:
            collide = True

        overlap = distance.magnitude - self.radius
        displacement = distance.normalize() * overlap

        return (collide, displacement)

