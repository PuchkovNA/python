__author__ = "Пучков Николай Александрович"
#1
class Data_(object):
    stroka = '2-09-2011'

    def __init__(self, stroka):
        self.stroka = stroka

    @classmethod
    def data_to_int(cls):
        return [int(el) for el in cls.stroka.split('-')]

    @staticmethod
    def check_d_m_y(self):
        if 0 > int(self.split('-')[1]) or 12 < int(self.split('-')[1]):
            print ( 'Месяц должен быть в диапазоне 1-12')


print(Data_.stroka)
a = Data_('1-11-2022')
print(a.stroka)
print(Data_.stroka)


class ChildClass(Data_):
    stroka = '2-09-2017'
    pass


print(Data_.data_to_int())
a = Data_('15-14-2022')

a.check_d_m_y('15-10-2022')

2
class ZeroDivisionError(Exception):
    pass


try:
    val = int(input("Введите делимое: "))
    val1 = int(input("Введите делитель: "))
    if val1 == 0:
        raise ZeroDivisionError("Деление на: " + str(val1))
    print(f' Результат деления {val} на {val1} = {val / val1}')
except ZeroDivisionError as e:
    print(e)

# 3

def example():
    ls = []

    while True:

        try:
            inpt = input("Введите число в список целых знаений:")
            if inpt == "stop":
                break
            ls.append(int(inpt))

        except ValueError:
            print("Error! Это не число, попробуйте снова.")


    print(ls)

example()

#4 #5 #6
class Sclad():
    # volume - макс.объем складского места
    # mass -  максимальная масса товара, которое можно разместить на складское место
    # размещение на склад производится на первое доступное место в номенклатуре которого есть данная категория
    sclad = {"mesto1": {"volume": [5], "mass": [300], "nomenklatura": {'Printer': [], 'Skaner': [], 'Xerox': []}},
             "mesto2": {"volume": [3], "mass": [100], "nomenklatura": {'Printer': []}}}
    department = {}

    def __init__(self, address):
        self.address = address

    def sclad_setter(self, object):
        for key in Sclad.sclad:
            print(sum(Sclad.sclad.get(key).get('volume')) - object.height * object.depth * object.length + sum(
                Sclad.sclad.get(key).get('mass')) - object.mass)
            if sum(Sclad.sclad.get(key).get('volume')) - object.height * object.depth * object.length > 0 and sum(
                    Sclad.sclad.get(key).get('mass')) - object.mass > 0:
                vol = Sclad.sclad.get(key).get('volume')
                vol.append(-object.height * object.depth * object.length)
                mass = Sclad.sclad.get(key).get('mass')
                mass.append(-object.mass)
                for key1 in Sclad.sclad.get(key).get('nomenklatura'):
                    if object.__class__.__name__ == key1:
                        Sclad.sclad.get(key).get('nomenklatura').get(key1).append(object.articul)
                dict = {key: {"volume": vol, "mass": mass, "nomenklatura": Sclad.sclad.get(key).get('nomenklatura')}}
                Sclad.sclad.update(dict)
                break
            else:
                print(f'Место {key} не может вместить товар')
                m = m + 1
        if m == len(Sclad.sclad):
            print(f'Склад по адресу {self.address} не может вместить товар')

    def sclad_setter(self, object, num=1):
        m = 0
        for i in range(num):
            for key in Sclad.sclad:
                if sum(Sclad.sclad.get(key).get('volume')) - object.height * object.depth * object.length > 0 and sum(
                        Sclad.sclad.get(key).get('mass')) - object.mass > 0:
                    vol = Sclad.sclad.get(key).get('volume')
                    vol.append(-object.height * object.depth * object.length)
                    mass = Sclad.sclad.get(key).get('mass')
                    mass.append(-object.mass)
                    for key1 in Sclad.sclad.get(key).get('nomenklatura'):
                        if object.__class__.__name__ == key1:
                            Sclad.sclad.get(key).get('nomenklatura').get(key1).append(object.articul)
                    dict = {
                        key: {"volume": vol, "mass": mass, "nomenklatura": Sclad.sclad.get(key).get('nomenklatura')}}
                    Sclad.sclad.update(dict)
                    break
                else:
                    print(f'Место {key} не может вместить товар')
                    m = m + 1
            if m == len(Sclad.sclad):
                print(f'Склад по адресу {self.address} не может вместить товар')

    def sclad_getter(self):
        return Sclad.sclad

    def department_getter(self):
        return Sclad.department

    def sclad_out(self, object):
        for key in Sclad.sclad:
            for x in Sclad.sclad.get(key).get('nomenklatura').keys():
                try:
                    ind = Sclad.sclad.get(key).get('nomenklatura').get(x).index(object.articul)
                    Sclad.sclad.get(key).get('volume').remove(-object.height * object.depth * object.length)
                    Sclad.sclad.get(key).get('mass').remove(-object.mass)
                    print(f'Артикул товара {object.articul} найден в категории товара {x}, место {key}')
                    if x == object.__class__.__name__:
                        Sclad.sclad.get(key).get('nomenklatura').get(x).pop(ind)
                        break
                except ValueError:
                    print(f'Артикул товара {object.articul} нет в категории товара {x}, место {key}')

    def sclad_out(self, object, department):
        for key in Sclad.sclad:
            for x in Sclad.sclad.get(key).get('nomenklatura').keys():
                try:
                    ind = Sclad.sclad.get(key).get('nomenklatura').get(x).index(str(object.articul))
                    Sclad.sclad.get(key).get('volume').remove(-object.height * object.depth * object.length)
                    Sclad.sclad.get(key).get('mass').remove(-object.mass)
                    Sclad.department.update({department: {object.articul: object.__class__.__name__}})
                    print(f'Артикул товара {object.articul} найден в категории товара {x}, место {key}')
                    if x == object.__class__.__name__:
                        Sclad.sclad.get(key).get('nomenklatura').get(x).pop(ind)
                        break
                except ValueError:
                    print(f'Артикул товара {object.articul} нет в категории товара {x}, место {key}')


class Orgtehnika():
    def __init__(self, mass, height, depth, length, color, producer, articul):
        self.mass = mass
        self.height = height
        self.depth = depth
        self.length = length
        self.color = color
        self.producer = producer
        self.articul = articul

    pass


class Printer(Orgtehnika):
    PRINTER_TYPE = ('laser', 'ink', 'needl')

    def __init__(self, mass, height, depth, length, color, producer, articul, speed, type, color_print: bool):
        self.mass = mass
        self.height = height
        self.depth = depth
        self.length = length
        self.color = color
        self.producer = producer
        self.articul = articul
        self.speed = speed
        self.type = type
        self.color_print = color_print


class Skaner(Orgtehnika):
    FORMAT = ('A3', 'A4')

    def __init__(self, mass, height, depth, length, color, producer, articul, speed, format: FORMAT):
        self.mass = mass
        self.height = height
        self.depth = depth
        self.length = length
        self.color = color
        self.producer = producer
        self.articul = articul
        self.speed = speed
        self.format = format


class Xerox(Orgtehnika):
    def __init__(self, mass, height, depth, length, color, producer, articul, speed, two_page: bool):
        self.mass = mass
        self.height = height
        self.depth = depth
        self.length = length
        self.color = color
        self.producer = producer
        self.articul = articul
        self.speed = speed
        self.two_page = two_page


# sclad =("dep1":[("skaner":)])
# sclad = {"mesto1": {"volume": (5, 7, 8, 12), "nomenklatura": ('printer', 'skaner', 'xerox')}}

pr1 = Printer(5, 0.5, 0.5, 0.5, 'черный', 'Россия', 'jjjdfq-123', 12, 'laser', True)
scld = Sclad('Москва, Красная площадь')
# Принятие на склад
scld.sclad_setter(pr1)
print(scld.sclad_getter())
# Списание со склада
# scld.sclad_out('jjjdfq-123',pr1.__class__.__name__)
# Списание со склада с передачей в Бухгалтерию
scld.sclad_out(pr1, 'Бухгалтерия')
print(scld.sclad_getter())
print(scld.department_getter())
pr2 = Xerox(10, 0.5, 1, 0.5, 'белый', 'Китай', 'jjjdfq-155', 12, True)
scld.sclad_setter(pr2)
print(scld.sclad_getter())
print(scld.department_getter())
# Принятие на склад с однинаковым артикулом товара
scld.sclad_setter(pr1, 3)
print(scld.sclad_getter())
# Списание со склада с передачей в Дирекцию
scld.sclad_out(pr1, 'Дирекция')
print(scld.sclad_getter())
print(scld.department_getter())
#7
class complex_num():
    def __init__(self, comp_num):
        self.comp_num = comp_num

    def __str__(self):
        print(self.comp_num)

    def __add__(self, other):

        i = self.comp_num+other.comp_num
        return complex_num(i)

    def  __mul__(self, other):

        i = self.comp_num*other.comp_num
        return complex_num(i)
i1 = complex_num(1+3j)
i2 = complex_num(2+4j)
(i1+i2).__str__()
(i1*i2).__str__()