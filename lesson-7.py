__author__ = "Пучков Николай Александрович"

from abc import ABC, abstractmethod


# 1
class Matrix():
    def __init__(self, *name):
        self.name = name

    def __str__(self):
        for ls in self.name:
            print(ls)

    def __add__(self, other):
        ls2 = []
        for ls in range(max(len(self.name), len(other.name))):
            ls3 = []
            for ls1 in range(max(len(self.name[0]), len(other.name[0]))):
                ls3.append(self.name[ls][ls1] + other.name[ls][ls1])
            ls2.append(ls3)
        return Matrix(*ls2)


mtr = Matrix([1, 5, 3], [5, 0, 7], [0, 7, 9])
mtr1 = Matrix([1, 2, 3], [5, 6, 7], [0, 2, 9])
mtr.__str__()
print('x' * 100)
(mtr + mtr1).__str__()
print('x' * 100)
mtr = Matrix([1, 7, 3, 5], [5, 6, 7, 3])
mtr1 = Matrix([1, 2, 3, 4], [5, 0, 7, 1])
(mtr + mtr1).__str__()
print('x' * 100)
mtr = Matrix([1, 2, 3], [5, 6, 7], [0, 8, 9], [1, 2, 3])
mtr1 = Matrix([1, 2, 3], [5, 6, 7], [0, 8, 9], [5, 6, 7])
(mtr + mtr1).__str__()
print('x' * 100)

#2
class Odejda(ABC):
    __s = 0

    def __init__(self, title):
        self.title = title

    @abstractmethod
    def s_tkani(self):
        pass

    @property
    def s(self):
        return type(self).__s

    @s.setter
    def s(self, val):
        type(self).__s = val


class Palto(Odejda):
    def __init__(self, title, V):
        super().__init__(title)
        self.V = V

    def s_tkani(self):
        return float(self.V) / 6.5 + 0.5


class Kostym(Odejda):
    def __init__(self, title, H):
        super().__init__(title)
        self.H = H

    def s_tkani(self):
        return 2 * self.H + 0.3


p = Palto('Пальто серое', 20)
k = Kostym('Костюм черный', 50)
print(f'{p.title} расход ткани {p.s_tkani()} M2')
print(f'{k.title} расход ткани {k.s_tkani()} M2')
Odejda.s = p.s_tkani() + k.s_tkani()
print(f'Общий расход ткани {Odejda.s} M2')


# 3
class Cell():
    def __init__(self, cells: int):
        self.cells = cells

    def __str__(self):
        print(self.cells)

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __sub__(self, other):
        if self.cells > other.cells:
            return Cell(self.cells - other.cells)
        else:
            return 'разность количества ячеек двух клеток меньше нуля'

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(self.cells // other.cells)

    def make_order(self, n: int):
        print(('*' * n + '\\n') * int(self.cells // n) + '*' * (self.cells % n))


a = Cell(5)
b = Cell(10)
(a + b).__str__()
(b - a).__str__()
(b / a).__str__()
(b * a).__str__()

b.make_order(3)

a.make_order(5)