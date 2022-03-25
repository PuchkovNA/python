__author__ = "Пучков Николай Александрович"


# 1
def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "На ноль нельзя делить"


a = int(input('Введите делимое число'))
b = int(input('Введите делитель'))

print(division(a, b))


# 2
def person_details(name, second_name, bithday, living_city, email, home_phone):
    print(
        f"Фамилия: {second_name}, Имя:{name}, Дата рождения:{bithday}, Город проживания:{living_city},Э лектронная почта:{email}, Домашний телефон:{home_phone}")


person_details(name="Иван", second_name="Иванов", bithday="15.03.1980", living_city="Москва", email="ivanov@pochta.ru",
               home_phone="47823783727")


# 3
def my_func(a, b, c):
    print(max([a + b, a + c, b + c]))


my_func(3, 5, 6)


# 4
def my_func1(x, y):
    print(x ** y)
my_func1(3, -4)

def my_func2(x, y, z=1):
    for i in range(abs(y)):
        print(x)
        z = z*x
    print(1/z)
my_func2(2, -3)

#5
def int_func():
    s = 0
    while True:
        li = input().split()
        for num in li:
            if num == '%':
                return print(s)
            else:
                s = s+int(num)
        print(s)
int_func()
#6
# Реализовать функцию int_func(),
# принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
def int_func(*args):
        for word in args:
                print(str(word).capitalize())
int_func("sdfsd","qqqeqwe")

#7
def int_func():
    while True:
        li = input().split()
        for word in li:
            if word == 'stop':
                return
            else:
                print(str(word).capitalize())
int_func()