__author__ = "Пучков Николай Александрович"


#1
# Скрипт сохраняется  файле script.py
from sys import argv
#(выработка в часах*ставка в час) + премия
a1, a2,a3 = map(int,argv[1:])
print(f"Зароботная плата = {a1*a2+a3}")

# Запуск скрипта в терминале python script.py 1 2 3
# Зароботная плата = 5

#2
li = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new = [ li[i] for i in range(1,len(li)) if (li[i] > li[i-1])  ]
print(new)
#3
new = [i for i in range(20,240) if i%20 == 0 or i%21 == 0]
print(new)
#4
li = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
new = [el for el in li if li.count(el)<2]
print(new)
#5
from functools import reduce

items = [i for i in range(100,1000)]
all = reduce(lambda x, y: x * y, items)

print(all)
#6
# Скрипт сохраняется  файле script.py
from itertools import count, cycle
for i in count(3):
    if i > 10:
        break
    print(i)
# Запуск скрипта в терминале python script.py

# Скрипт сохраняется  файле script.py
from itertools import count, cycle

i = 0
for el in cycle(['erqwer', 342, 'qewrqew', 3322, 2323]):
    i += 1
    if i > 2:
        break
    print(el)

# Запуск скрипта в терминале python script.py

#7
def fact(n):
    a = 1
    for i in range(1, n + 1):
        a *= i
        yield a


for x in fact(6):
    print(x)