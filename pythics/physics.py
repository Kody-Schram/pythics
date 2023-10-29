from time import perf_counter

class Physics:

    instance = None

    def __init__(self):
        if Physics.instance is None:
            Physics.instance = self

        self.objects = set()

        self.running = True

        self.deltaTime = 0
        self._last = 0

    def update(self):
        current = perf_counter()
        self.deltaTime = current - self._last
        self._last = current

        for obj in self.objects:
            obj.update(self.deltaTime)

    def loop(self):
        while self.running:
            self.update()


if __name__ == '__main__':
    from object import Object
    physics = Physics()
    obj = Object()
