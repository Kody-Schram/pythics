from utils.vector import Vector
from utils.funcs import *

import time

last = time.perf_counter()
current = time.perf_counter()
deltaTime = current - last

def simulate():
    global current
    last = current
    current = time.perf_counter()
    deltaTime = current - last