from pythics.vector import Vector
from pythics.utils.funcs import clamp
from pythics.physics import Physics
from pythics.utils.errors import NoEngine

import math



class Collider:
    def __init__(self, x, y, no_engine=False, trigger=False, relative=True, parent=None) -> None:
        self.x = x
        self.y = y

        self.trigger = trigger
        self.no_engine = no_engine
        self.relative = relative
        self.parent = parent


        if not no_engine or not trigger:
            try:
                Physics.instance.add_collider(self)
            except AttributeError as e:
                raise NoEngine(f'\n \n {self} could not find a Physics instance. To create a collider without using the Physic Engine, enter (no_engine=True) when creating a Collider.\n')



    def displace(self, movement):
        # Moves colliders position
        self.x += movement.x
        self.y += movement.y

        # Only moves parent if it HAS a parent and IS relative to their position
        if not self.parent == None and self.relative:
            self.parent.x += movement.x
            self.parent.y += movement.y


            # Reseting gravity if it hits object
            if not self.parent.gravity.x == 0:
                self.parent.velocity.x = 0

            if not self.parent.gravity.y == 0:
                self.parent.velocity.y = 0




# Basic rect or square collider
class BoxCollider (Collider):
    def __init__(self, x, y, width, height, no_engine=False, trigger=False, relative=True, parent=None) -> None:
        super().__init__(x, y, no_engine=no_engine, trigger=trigger, relative=relative, parent=parent)
        
        self.width = width
        self.height = height
        


    # Quality of life functions
    @property
    def position(self) -> Vector:
        return Vector(self.x, self.y)


    @property
    def as_tup(self):
        return (self.position.x, self.position.y, self.width, self.height)
    

    @property
    def center(self):
        return (self.x + (self.width / 2), self.y + (self.height / 2))



    def collide(self, other):
        if isinstance(other, BoxCollider):
            return self.collide_rect(other)

        elif isinstance(other, CircleCollider):
            return self.collide_circle(other)



    # Collision detection functions
    def collide_point(self, point: Vector) -> bool:
        """Returns -> (bool, Vector)
           Bool: Collision occured
           Vector: Displacement vector
           
           Determines if the current object(BoxCollider) collides with a point(Vector)"""


        return (self.x <= point.x and self.x + self.width >= point.x) and (self.y <= point.y and self.y + self.height >= point.y)


    def collide_rect(self, rect):
        """Returns -> (bool, Vector)
           Bool: Collision occured
           Vector: Displacement vector
           
           Determines if the current object(BoxCollider) collides with a given collider(BoxCollider)"""
        

        collide = False

        # Collision detection
        if (self.x <= rect.x + rect.width and self.x + self.width >= rect.x) and (self.y <= rect.y + rect.height and self.y + self.height >= rect.y):
            collide = True


        # Displacement calculation
        closest_s = Vector(clamp(rect.center[0], self.x, self.x + self.width), clamp(rect.center[1], self.y, self.y + self.height))
        closest_o = Vector(clamp(self.center[0], rect.x, rect.x + rect.width), clamp(self.center[1], rect.y, rect.y + rect.height))

        displacement = closest_o - closest_s


        return (collide, displacement)


    def collide_circle(self, circle):
        collision = circle.collide_rect(self)
        print('rect on circle', collision)


        return (collision[0], collision[1])

    


class CircleCollider(Collider):
    def __init__(self, x, y, radius, no_engine=False, trigger=False, relative=True, parent=None) -> None:
        super().__init__(x, y, no_engine=no_engine, trigger=trigger, relative=relative, parent=None)
        
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
           Bool: Collision occured
           Vector: Displacement vector
           
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

