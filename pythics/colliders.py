from abc import ABC, abstractmethod

from .vector import Vector

class Collider:
    @abstractmethod
    def collide(self) -> (bool, Vector):
        ...

class BoxCollider(Collider):
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def collide(self) -> (bool, Vector):
        ...