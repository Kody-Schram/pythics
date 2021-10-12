import pythics.colliders as colliders
import pythics.vector as vector
import pythics.utils.funcs as funcs

import time
import copy

class Physics:
    instance = None

    def __init__(self, chunk_size=250) -> None:
        self.chunks = {}
        self.objects = []
        self.chunk_size = chunk_size
        self.triggers = {}

        self.deltaTime = time.perf_counter()
        self._last = time.perf_counter()


        # Makes class a singleton
        if Physics.instance == None:
            Physics.instance = self

    

    def add_collider(self, collider):
        """The user does NOT have to call this function.
        It will be called when creating a new BoxCollider or CircleCollider object
        """

        if collider.trigger:
            self.triggers[collider] = False
        

        # chunk = funcs.determine_chunk(collider.x, collider.y, self.chunk_size)
        chunk = (round(collider.x / self.chunk_size), round(collider.y / self.chunk_size))
        try:
            self.chunks[chunk].add(collider)

        except KeyError as e:
            self.chunks[chunk] = set()
            self.chunks[chunk].add(collider)
    
    

    def add_object(self, object):
        self.object.append(object)



    def run(self):
        # Delta time calculation
        current_time = time.perf_counter()
        self.deltaTime = current_time - self._last
        self._last = current_time

        for object in self.objects:
            object.simulate()


        # print(self.triggers)
        # Resets trigger activations
        for trigger in funcs.k2l(self.triggers):
            self.triggers[trigger] = False


        # Collision detection
        for chunk in funcs.k2l(self.chunks):
            for collider1 in self.chunks[chunk]:
                for collider2 in self.chunks[chunk]:

                    # Collider can't collide with itself
                    if collider1 is collider2:
                        continue

                    else:
                        if not collider1.trigger and not collider2.trigger:
                            if not collider1.static:
                                # Displaces collider1 if it's not static
                                collision = collider1.collide(collider2)

                                if collision[0]:
                                    collider1.displace(collision[1])
                            

                            elif not collider2.static:
                                # Displaces collider2 if it's not static and collider1 was
                                collision = collider2.collide(collider1)

                                if collision[0]:
                                    collider2.displace(collision[1])


                            else: # Continues loop if both are static, just lets them collide
                                continue


                        # If one or both are triggers
                        else:

                            # Trigger detection for collider1
                            if collider1.trigger:
                                # Only detects if allowed
                                if collider2 in collider1.detects or True in collider1.detects:
                                    collision = collider1.collide(collider2)

                                    if collision[0]:
                                        self.triggers[collider1] = True


                            # Trigger detection for collider2
                            if collider2.trigger:
                                # Only detects if allowed
                                if collider1 in collider2.detects or True in collider2.detects:
                                    collision = collider2.collide(collider1)

                                    if collision[0]:
                                        self.triggers[collider2] = True




        # for chunk in funcs.k2l(self.chunks):
        #     search = copy.copy(self.chunks[chunk])

        #     for collider1 in search:
        #         temp = copy.copy(self.chunks[chunk])
        #         temp.remove(collider1)
        #         others = set()

        #         if collider1.trigger:
        #             try:
        #                 temp2 = copy.copy(collider1.detects)
        #                 temp2.remove(True)
                        
        #                 others = temp.intersection(temp)

        #             except KeyError:
        #                 others = temp

        #         else:
        #             others = temp

        #         for collider2 in others:
        #             print(collider1.trigger, collider2.trigger)

        #             if not collider1.trigger and not collider2.trigger:
        #                 collision = collider1.collide(collider2)
        #                 if collision[0]:
        #                     if not collider1.static:
        #                         collider1.displace(collision[1])
                            
        #                     else:
        #                         collider2.displace(collision[1] * -1)
                    
        #             else:
        #                 if collider1.trigger:
        #                     if True in collider1.detects or collider2 in collider1.detects:
        #                         self.triggers[collider1] = True
                        
        #                 if collider2.trigger:
        #                     if True in collider2.detects or collider1 in collider2.detects:
        #                         self.triggers[collider2] = True

                        
