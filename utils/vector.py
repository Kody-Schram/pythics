import math

class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y


    @property
    def magnitude(self) -> float:
        return math.sqrt(self.x**2 + self.y**2)

    @property
    def as_tup(self):
        return (self.x, self.y)

    def dot(self, other: 'Vector') -> float:
        return self.x * other.x + self.y * other.y


    def __repr__(self) -> str:
        return f'({self.x}, {self.y})'


    def sub(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def add(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)

    def scale(self, scalar: int) -> 'Vector':
        return Vector(self.x * scalar, self.y * scalar)



if __name__ == '__main__':
    pass