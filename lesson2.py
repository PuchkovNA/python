__author__ = "Пучков Николай Александрович"
# 1
lst = [0,0.1,'hi',True,'wow',['1'],{'1'},0x14,0b1,{'short': 'dict', 'long': 'dictionary'}]
for i in lst:
    print(type(i))

# 2
my_lst = []
ln = input('введите длину списка:')

for i in range(int(ln)):
    my_lst.append(input('введите элемент списка:'))
print(my_lst)
for i in my_lst[1::2]:
    ind = my_lst.index(i)
    my_lst[ind] , my_lst[int(ind-1)] = my_lst[int(ind-1)],  my_lst[ind]

print(my_lst)
#3
lst = ['','зима','зима', 'весна','весна','весна','лето','лето','лето','осень','осень','осень','зима',]
month = input('введите порядковый номер месяца:')
if 0 < int(month) < 13:
    print(lst[int(month)])
else:
    print('Недопустимый номер месяца')

dict = {'1':'зима','2':'зима','12':'зима','3':'весна','4':'весна','5':'весна', '6': 'лето', '7': 'лето','8': 'лето','9': 'осень','10': 'осень','11': 'осень'}
month = input('введите порядковый номер месяца:')
if 0 < int(month) < 13:
    print(dict[month])
else:
    print('Недопустимый номер месяца')
#4
in_str = input('введите строку из нескольких слов, разделённых пробелами:')
lst = in_str.split()
for i in lst:
    print(i[0:10])
#5
my_list = [7, 5, 3, 3, 2]
my_rank = int(input('введите рейтинг:'))
my_list.insert(my_list.index(my_rank),my_rank)
print(my_list)
#6
my_list = []
my_dict = {}

key_list = ['название', 'цена', 'количество', 'eд']
for i in range(int(input('введите количество товаров'))):
    d = {a: input(a) for a in key_list}
    my_list.append((i + 1, d))
index = 0
my_dict = {}
for i in my_list:
    for el in my_list[index][1]:
        lst = []
        for x in range(len(my_list)):
            lst.append((my_list[x][1]).get(el))
        my_dict[el] = lst
    index = index + 1
print(my_dict)
