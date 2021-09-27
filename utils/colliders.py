from pythics.utils.vector import Vector
from pythics.utils.funcs import clamp
from pythics.physics import Physics
from pythics.utils.errors import NoEngine

import math

# Basic rect or square collider
class BoxCollider:
    def __init__(self, x, y, width, height, no_engine=False, trigger=False) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.trigger = trigger

        if not no_engine or not trigger:
            try:
                Physics.instance.add_collider(self)
            except AttributeError as e:
                raise NoEngine(f'\n \n {self} could not find a Physics instance. To create a collider without using the Physic Engine, enter (no_engine=True) when creating a Collider.\n')



    # Quality of life functions
    @property
    def position(self) -> Vector:
        return Vector(self.x, self.y)

    @property
    def as_tup(self):
        return (self.position.x, self.position.y, self.width, self.height)

    

    def collide(self, other):
        if isinstance(other, BoxCollider):
            return self.collide_rect(other)

        elif isinstance(other, CircleCollider):
            return self.collide_circle(other)

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

    def collide_circle(self, circle):
        return circle.collide_rect(self)

    
class CircleCollider:
    def __init__(self, x, y, radius, no_engine=False, trigger=False) -> None:
        self.x = x
        self.y = y
        self.radius = radius
        self.trigger = trigger

        if not no_engine:
            try:
                Physics.instance.add_collider(self)
            except AttributeError as e:
                raise NoEngine(f'\n \n {self} could not find a Physics instance. To create a collider without using the Physic Engine, enter (no_engine=True) when creating a Collider.\n')



    # Quality of life functions
    @property
    def position(self) -> Vector:
        return Vector(self.x, self.y)
    
    @property
    def as_tup(self):
        return (self.x, self.y, self.width, self.height)



    def collide(self, other):
        if isinstance(other, CircleCollider):
            return self.collide_circle(other)

        elif isinstance(other, BoxCollider):
            return self.collide_rect(other)

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

        distance = self.position - other.position
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

