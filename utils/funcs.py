# Clamping function
def clamp(n, lo, hi):
    """Returns value if within range.
    If not in range, will return either lo or hi value, based on value of n"""
    return max(lo, min(n, hi))


def determine_chunk(x, y, chunk_size):
    aprox_x = round(x / chunk_size)
    aprox_y = round(y / chunk_size)

    return (aprox_x, aprox_y)