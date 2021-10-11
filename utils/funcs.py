from pythics.colliders import *

# Clamping function
def clamp(n, lo, hi):
    """Returns value if within range.
    If not in range, will return either lo or hi value, based on value of n"""
    return max(lo, min(n, hi))


def determine_chunk(obj, chunk_size):
    aprox_x = round(obj.x / chunk_size)
    aprox_y = round(obj.y / chunk_size)

    chunks = [(aprox_x, aprox_y)]

    # if isinstance(obj, BoxCollider):
        
    # return chunks


def k2l(dict):
    """Dictionary keys to list"""
    return list(dict.keys())
