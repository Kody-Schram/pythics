import pythics.colliders as colliders
import pythics.vector as vector
import pythics.utils.funcs as funcs

import time

class Physics:
    instance = None

    def __init__(self, chunk_size=250) -> None:
        self.chunks = {}
        self.objects = []
        self.chunk_size = chunk_size
        self.triggers = {}

        # Makes class a singleton
        if Physics.instance == None:
            Physics.instance = self

        self.deltaTime = time.perf_counter()
        self._last = time.perf_counter()

    
    def add_collider(self, collider):
        """The user does NOT have to call this function.
        It will be called when creating a new BoxCollider or CircleCollider object
        """

        if collider.trigger:
            self.triggers[collider] = False
        
        # chunk = funcs.determine_chunk(collider.x, collider.y, self.chunk_size)
        chunk = (round(collider.x / self.chunk_size), round(collider.y / self.chunk_size))
        try:
            self.chunks[chunk].append(collider)

        except KeyError as e:
            self.chunks[chunk] = [collider]

    def add_object(self, object):
        self.object.append(object)


    def check_collision(self, obj):
        chunk = funcs.determine_chunk()

    def run(self):
        # Delta time calculation
        current_time = time.perf_counter()
        self.deltaTime = current_time - self._last
        self._last = current_time

        for object in self.objects:
            object.simulate()


        # Resets trigger activations
        for trigger in funcs.k2l(self.triggers):
            self.triggers[trigger] = False

        # Collision detection
        for chunk in funcs.k2l(self.chunks):
            for collider1 in self.chunks[chunk]:
                for collider2 in self.chunks[chunk]:

                    # print(collider1 in funcs.k2l(self.triggers), collider2 in funcs.k2l((self.triggers)))

                    if not collider1.trigger and not collider2.trigger:
                        collision = collider1.collide(collider2)
                        if collision[0]:
                            collider1.displace(collision[1])
                            print(collision)
                    
                    elif collider1.trigger:
                        self.triggers[collider1] = True
                    
                    elif collider2.trigger:
                        self.triggers[collider2] = True
