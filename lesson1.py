__author__ = "Пучков Николай Александрович"
# 1
a = 10
print(a)
b = 'Hello world'
print(b)
c = int(input('Введите ваш возраст:'))
print('Ваш возраст:', c)
d = input('Введите ваше имя:')
print('Ваше имя:', d)

# 2
sec = int(input('Введите время в секундах:'))
hours = sec // 3600
minutes = (sec - hours * 3600) // 60
secundes = sec - hours * 3600 - minutes * 60

print('Время в формате "чч:мм:сс" {:02d}:{:02d}:{:02d}'.format(hours, minutes, secundes))

# 3
num = input('Введите целое число:')
summa = 0
index = 1
while index < int(num) + 1:
    summa += int(num * index)
    index += 1
print(summa)
# 4
print(max(list(input('Введите число:'))))
# =====================================================
num = input('Введите число:')
index = 0
cifer1 = 0
while index < len(num):
    cifer = int(num[index])
    if cifer1 < cifer:
        cifer1 = cifer
    index += 1
print(cifer1)
# =======================================================
num = int(input('Введите число:'))
max = 0
while num > 0:
    division = num % 10
    if max <= division:
        max = division
    num = num // 10
print(max)
# 5
expenses = float(input('Введите издержки :'))
gross = float(input('Введите выручку :'))
if gross >= expenses:
    print('Прибыль :', gross - expenses)
else:
    print('Убыток :', expenses - gross)

# 6
expenses = float(input('Введите издержки :'))
gross = float(input('Введите выручку :'))
if gross >= expenses:
    print('Прибыль :', gross - expenses, '.руб')
    print('Рентабельность в %:', (gross - expenses) * 100 / gross)
    employers = int(input('Введите количество работников :'))
    print('Прибыль в расчете на одного сотрудника:', (gross - expenses) / employers, '.руб')
else:
    print('Убыток :', expenses - gross)

# 7
a = int(input('Первый день километров :'))
b = int(input('Цель: пробежать километров :'))
i = 1
while a < b:
    a += a * 0.1
    print(i, '-й день:', '{:10.2f}'.format(a))
    i += 1
