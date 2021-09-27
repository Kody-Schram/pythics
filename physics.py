import pythics.utils.rigidbody as rb
import pythics.utils.colliders as colliders
import pythics.utils.vector as vector
import pythics.utils.funcs as funcs

import time
import asyncio

class Physics:
    instance = None

    def __init__(self, running, chunk_size=250) -> None:
        self.running = running
        self.chunks = {}
        self.rigibodies = []
        self.chunk_size = chunk_size

        # Prevents duplicate Physics instances
        # Also allows for the instance to be accessed by other files
        # without passing in the variable for the instance
        if Physics.instance == None:
            Physics.instance = self
    
    def add_collider(self, collider):
        """The user does NOT have to call this function.
        It will be called when creating a new BoxCollider or CircleCollider object
        """
        
        chunk = funcs.determine_chunk(collider.x, collider.y, self.chunk_size)
        try:
            self.chunks[chunk].append(collider)

        except KeyError as e:
            self.chunks[chunk] = [collider]


    def run(self):
        while self.running:
            for chunk in funcs.k2l(self.chunks):
                for collider1 in self.chunks[chunk]:
                    for collider2 in self.chunks[chunk]:
                        print(collider1, collider2)
                        if collider1.collide(collider2):
                            print('collided')
