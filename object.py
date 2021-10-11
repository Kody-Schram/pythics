from .vector import Vector
from pythics.physics import Physics
from .utils.errors import NoEngine

class Object:
    def __init__(self, x, y, gravity = Vector(0, 1), velocity = Vector(0, 0), collider=None, no_engine=False) -> None:
        self.x, self.y = x, y
        self.gravity = gravity
        self.velocity = velocity
        self.collider = collider

        if not collider == None:
            collider.parent = self

        Physics.instance.objects.append(self)


    
    def simulate(self, deltaTime=None) -> None:
        self.velocity.x += self.gravity.x * 1.5
        self.velocity.y += self.gravity.y * 1.5

        if deltaTime == None:
            try:
                self.x += self.velocity.x * Physics.instance.deltaTime
                self.y += self.velocity.y * Physics.instance.deltaTime

                if not self.collider == None:
                    if self.collider.relative:
                        self.collider.x += self.velocity.x * Physics.instance.deltaTime
                        self.collider.y += self.velocity.y * Physics.instance.deltaTime
            
            except AttributeError as e:
                raise NoEngine('There is no engine to get deltaTime from. To use rigidbodies, there must be a Physics class instance. Either that or manually pass in a value for the deltaTime kwarg.')
        
        else:
            self.x += self.velocity.x * deltaTime
            self.y += self.velocity.y * deltaTime

            if not self.collider == None:
                if self.collider.relative:
                    self.collider.x += self.velocity.x * deltaTime
                    self.collider.y += self.velocity.y * deltaTime
