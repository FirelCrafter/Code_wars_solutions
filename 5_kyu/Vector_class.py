from itertools import zip_longest


class Vector:
    def __init__(self, *nums):
        self.numbers = list(*nums) if len(nums) == 1 else list(nums)

    def __str__(self):
        return '<{}>'.format(', '.join([str(n) for n in self.numbers]))

    def __add__(self, other):
        return Vector([b + t for b, t in zip_longest(self.numbers, other.numbers)])

    def __sub__(self, other):
        return Vector([b - t for b, t in zip_longest(self.numbers, other.numbers)])

    def __eq__(self, other):
        return self.numbers == other.numbers

    @property
    def magnitude(self):
        return sum(v ** 2 for v in self.numbers) ** 0.5

    def dot(self, other):
        return sum(b * t for b, t in zip_longest(self.numbers, other.numbers))

    def to_tuple(self):
        return tuple(self.numbers)

    def cross(self, other):
        return Vector((self.numbers[1]*other.numbers[2] - self.numbers[2]*other.numbers[1]),
                      (self.numbers[2]*other.numbers[0] - self.numbers[0]*other.numbers[2]),
                      (self.numbers[0]*other.numbers[1] - self.numbers[1]*other.numbers[0]))

    @property
    def x(self):
        return self.numbers[0]

    @property
    def y(self):
        return self.numbers[1]

    @property
    def z(self):
        return self.numbers[2]


v = Vector(4, 5, 6)
v_2 = Vector([1, 2, 3])

print(v)
print(v_2)

print(v.x())
print(v_2.x())

print(v.to_tuple())
print(v_2.to_tuple())

print(v + v_2)
print(v - v_2)
print(v == v_2)

print(v.magnitude())
print(v_2.magnitude())

print(v.dot(v_2))
print(v.cross(v_2))






