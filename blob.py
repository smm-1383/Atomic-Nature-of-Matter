class Blob:
    def __init__(self):
        self.pixs = []
        self.middle = None

    def __str__(self):
        x, y = self.middle
        return f'{self.mass()} ({x:.4f}, {y:.4f})'

    def __repr__(self):
        return self.__str__()

    def add(self, x, y):
        self.pixs.append((x, y))
        self.middle = (sum(i[1] for i in self.pixs) / self.mass(),
                       sum(i[0] for i in self.pixs) / self.mass())

    def mass(self):
        return len(self.pixs)

    def distanceTo(self, other):
        (x, y), (xx, yy) = self.middle, other.middle
        return ((xx - x) ** 2 + (yy - y) ** 2) ** 0.5