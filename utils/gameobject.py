from vectors import Vector2

class GameObject:
    def __init__(self, name:str, tags, position: Vector2, layer: int) -> None:
        self.name:str = name
        self.tags = tags
        self.position: Vector2 = position
        self.layer: int = layer
        self.components = {}

    
    def getComponent(self, type):
        return self.components[type]


    def __repr__(self) -> str:
        return f'GameObject: "{self.name}" at position, ({self.position.x}, {self.position.y})'


if __name__ == '__main__':
    obj = GameObject('Test', [], Vector2(1, 1), 1)
    obj.components[Vector2] = Vector2(4, 4)
    print(obj.getComponent(Vector2))
