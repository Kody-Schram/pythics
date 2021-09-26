# Clamping function
def clamp(n, lo, hi):
    """Returns value if within range.
    If not in range, will return either lo or hi value, based on value of n"""
    return max(lo, min(n, hi))
