from .vector import Vector
from pythics.physics import Physics
from .utils.errors import NoEngine

class Object:
    def __init__(self, x, y, gravity = Vector(0, 1), velocity = Vector(0, 0), colliders=None, no_engine=False) -> None:
        self.x, self.y = x, y
        self.gravity = gravity
        self.velocity = velocity
        self.colliders = colliders

        for collider in self.colliders:
            if not collider == None:
                collider.parent = self

        Physics.instance.objects.append(self)


    def displace(self, movement):
        self.x += movement.x
        self.y += movement.y

        if movement.x > movement.y:
            move_x = False

        else:
            move_x = True


        # Reseting gravity if it hits object
        if not self.gravity.x == 0 and move_x:
            self.velocity.x = 0

        if not self.gravity.y == 0 and not move_x:
            self.velocity.y = 0


        for collider in self.colliders:
            if collider.relative:
                collider.x += movement.x
                collider.y += movement.y


    
    def simulate(self, deltaTime=None) -> None:
        self.velocity.x += self.gravity.x * 1.5
        self.velocity.y += self.gravity.y * 1.5

        if deltaTime == None:
            try:
                self.x += self.velocity.x * Physics.instance.deltaTime
                self.y += self.velocity.y * Physics.instance.deltaTime

                if not self.colliders == None:
                    for collider in self.colliders:
                        if collider.relative:
                            collider.x += self.velocity.x * Physics.instance.deltaTime
                            collider.y += self.velocity.y * Physics.instance.deltaTime
            
            except AttributeError as e:
                raise NoEngine('There is no engine to get deltaTime from. To use rigidbodies, there must be a Physics class instance or a manually passed in value for the deltaTime kwarg.')
        
        else:
            self.x += self.velocity.x * deltaTime
            self.y += self.velocity.y * deltaTime

            if not self.colliders == None:
                for collider in self.colliders:
                    if collider.relative:
                        collider.x += self.velocity.x * deltaTime
                        collider.y += self.velocity.y * deltaTime
