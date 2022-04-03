__author__ = "Пучков Николай Александрович"
#1
import time
class TrafficLight(object):

    def __init__(self, color):
        self.__color = color
    def running(self):
      if self.__color == "red":
          print(self.__color)
          time.sleep(7)
          print('orange')
          time.sleep(2)
          print('green')
          time.sleep(5)
      elif self.__color == "orange":
          print(self.__color)
          time.sleep(2)
          print('green')
          time.sleep(5)
          print('red')
          time.sleep(7)
      elif self.__color == "green":
          print(self.__color)
          time.sleep(5)
          print('red')
          time.sleep(7)
          print('orange')
          time.sleep(2)
trf = TrafficLight("red")
trf.running()
trf = TrafficLight("orange")
trf.running()
trf = TrafficLight("green")
trf.running()
#2
class Road(object):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width


    def mass_count(self):
        massa = self.__length*self.__width*float(input('Ввведите массу в кг на 1 м2 площади и высотой 1 см:'))*float(input('Ввведите высоту полотна дороги в см:'))/1000
        print(f'{massa} Т')

road = Road(20, 5000)
road.mass_count()
#3
class Worker():
    # name, surname, position(должность), income(доход);
    def __init__(self, name, surname, position, income:dict):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):

    def get_full_name(self):
        print(f'Имя сотрудника {self.name}  {self.surname}')

    def get_total_income(self):
        print(f'дохода с учётом премии {self._income.get("wage")+self._income.get("bonus")}')


pos = Position('Иван', 'Иванов', 'директор', {'wage':23423,'bonus':23423})
pos.get_full_name()
pos.get_total_income()
#4
class Car():

    def __init__(self, speed, color, name, is_police: bool):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def stop(self):
        return "Машина остановилась"

    def go(self):
        return "Машина поехала"

    def turn(self, dir):
        Car.dir = dir
        return f'Машина повернула на {self.dir}'

    def show_speed(self):
        return f' Скорость автомобиля {self.speed}'


class SportCar(Car):
    pass

class PoliceCar(Car):
    pass

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f' Скорость автомобиля превышает лимит {self.speed}'
        else:
            return f' Скорость автомобиля {self.speed}'

class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f' Скорость автомобиля превышает лимит {self.speed}'
        else:
            return f' Скорость автомобиля {self.speed}'
pol_car = PoliceCar(40, 'red', 'mustang', True)
print(pol_car.show_speed())
print(f'Полицеская машина {pol_car.is_police}')
work_car = WorkCar(50, 'Зеленая', 'Трактор', False)
print(work_car.show_speed())
town_car = TownCar(50, 'Желтая', 'Такси', False)
print(town_car.show_speed())
sport_car = SportCar(150, 'Черная', 'Lamborgini', False)
print(sport_car.show_speed())


#5

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pencil(Stationary):

    def draw(self):
        print(f' {self.title} с синими чернилами')


class Pen(Stationary):
    def draw(self):
        print(f'Чертеж выполнен {self.title}ом')


class Handle(Stationary):
    def draw(self):
        print(f'Для рисования на специальной доске {self.title}')

stat = Stationary('маркер')
stat.draw()
pencil = Pencil('ручка')
pencil.draw()
pen = Pen('карандаш')
pen.draw()
handle = Handle('маркер')
handle.draw()