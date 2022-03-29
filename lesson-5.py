__author__ = "Пучков Николай Александрович"

# 1. Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.

my_file = open("test.txt", "w+")
while True:
    st = input('Введите строку файла')
    if st == '':
        break
    else:
        my_file.writelines(st+'\n')
my_file.close()

# 2. Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

my_file = open("C:/Users/npuch/python/test.txt", 'r+')
print(my_file.read())
my_file.seek(0, 2)
while True:
    st = input('Введите строку файла')
    if st == '':
        break
    else:
        my_file.writelines(st+'\n')
my_file.close()
# 3. Создать текстовый файл (не программно). Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк). Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
my_file = open("C:/Users/npuch/python/test1.txt", 'r+', encoding="utf-8")
dic = {}
lines = my_file.readlines()
for line in lines:
    key,value = line.split()
    dic.update({key:value})
print(dic)
print(dic.values())
sum = 0
for x, y in dic.items():
    if float(y) > 20000:
        print(x, y)
    sum += float(y)
print(f'среднее:{sum/len(dic)}')

# 4. Создать (не программно) текстовый файл со следующим содержимым:
my_file1 = open("test3.txt", "w+")
dict = {'One':'Один', 'Two':'Два','Three':'Три','Four':'Четыре'}
my_file = open("C:/Users/npuch/python/test2.txt", 'r+', encoding="utf-8")
lines = my_file.readlines()
print(lines)
for line in lines:
    key = line.split('—')[0]
    print(key)
    newline = line.replace(key.strip(),dict[key.strip()])
    print(newline)
    my_file1.writelines(newline)

my_file.close()
my_file1.close()


# Напишите программу, открывающую файл на чтение и считывающую построчно данные. При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.
# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами. Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
my_file = open("test4.txt", "w+")
sum = 0
while True:
    st = input('Введите числа разделенный пробелом')
    if st == '':
        break
    else:
        my_file.writelines(st+'\n')
        for i in list(map(lambda c: float(c) ,st.split())):
            sum+=i
print(sum)
my_file.close()

# 6. Сформировать (не программно) текстовый файл. В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету. Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
my_file = open("C:/Users/npuch/python/test5.txt", 'r+', encoding="utf-8")
lines = my_file.readlines()

str = ''
dic ={}
print(lines)
for line in lines:
    lst = []
    sum = 0
    key = line.split(':')[0]
    for i in line.split(':')[1]:
        if 58 > ord(i) > 47:
            str+=i
        else:
            lst.append(str)
            str = ''
    for z in list(map(lambda c: int(c), list(filter(None, lst)))):
        sum += z
    dic.update({key: sum})
print(dic)

my_file.close()

# 7. Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
import json
my_file = open("test6.txt", "w+")
dic = {}
dic1 = {}
lst = []
sum = 0
while True:
    st = input('Введите данные о фирме: название, форма собственности, выручка, издержки:')
    if st == '':
        break
    else:
        my_file.writelines(st + '\n')
my_file.seek(0, 0)
lines = my_file.readlines()
sum = 0
i = 0
for line in lines:
    key = line.split()[0]
    dic.update({line.split()[0]: line.split()[3]})
    if float(line.split()[3]) > 0:
        i += 1
        sum += float(line.split()[3])
average_profit = sum / i
dic1.update({'average_profit': average_profit})

lst.append(dic)
lst.append(dic1)
print(lst)
jsonString = json.dumps(lst)
my_file2 = open("test7.txt", "w+")
my_file2.write(jsonString)
my_file2.close()
