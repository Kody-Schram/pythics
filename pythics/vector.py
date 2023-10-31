import math

class Vector:
    # Initializing function
    def __init__(self, x: float = 0, y: float = 0) -> None:
        if type(x) is tuple:
            self.x: float = x[0]
            self.y: float = x[1]

            return

        self.x: float = x
        self.y: float = y


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

    def __mul__(self, scalar: int) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar: int) -> 'Vector':
        return Vector(self.x / scalar, self.y / scalar)