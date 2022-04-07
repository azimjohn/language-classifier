import math


class Vector:
    def __init__(self, values):
        self.values = values

    def scale(self, n: float) -> 'Vector':
        values = list(self.values)
        for i, value in enumerate(values):
            values[i] = value * n
        return Vector(values)

    def product(self, other) -> float:
        total = 0
        for x, y in zip(self.values, other.values):
            total += x * y
        return total

    def normalize(self) -> 'Vector':
        length = self.length()
        for i, val in enumerate(self.values):
            self.values[i] = val / length
        return self

    def length(self) -> float:
        total = 0
        for val in self.values:
            total += val ** 2
        return math.sqrt(total)

    def copy(self):
        return Vector(self.values.copy())

    def __mul__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return self.scale(other)
        return self.product(other)

    def __repr__(self):
        return f"<{self.values}>"

    def __add__(self, other):
        values = []
        for x, y in zip(self.values, other.values):
            values.append(x + y)
        return Vector(values)
