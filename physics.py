import Objects.rigidbody as rb
import Objects.colliders as colliders
import utils.vector as vector
import utils.funcs as funcs


import time

last = time.perf_counter()
current = time.perf_counter()
deltaTime = current - last


rigid = rb.RigidBody(10, 10, 1, vector.Vector(0, 0))

def simulate():
    global current
    last = current
    current = time.perf_counter()
    deltaTime = current - last

    rigid.simulate()
    print(rigid.x, rigid.y)


while True:
    simulate()