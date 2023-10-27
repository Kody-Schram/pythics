import math

class Vector:
    # Quick directional vectors
    @property
    def down() -> 'Vector':
        return Vector(0, -1)

    @property
    def up() -> 'Vector':
        return Vector(0, 1)

    @property
    def left() -> 'Vector':
        return Vector(-1, 0)

    @property
    def right() -> 'Vector':
        return Vector(1, 0)

    @property
    def zero() -> 'Vector':
        return Vector(0, 0)

    # Initializing function
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


    # Quality of life functions
    @property
    def as_tup(self):
        return (self.x, self.y)

    def __repr__(self) -> str:
        return f'<{self.x}, {self.y}>'

    # Vector functions
    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    def normalize(self) -> 'Vector':
        mag = self.magnitude
        return Vector(self.x / mag, self.y / mag)

    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y

    # Operations
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar: float) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: float) -> 'Vector':
        return Vector(self.x / scalar, self.y / scalar)