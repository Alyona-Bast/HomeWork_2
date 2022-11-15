from math import pi
from math import e


printed = 5
count = int(input('Введите количество повторов: '))
print(printed * count)
print(pi * printed * count)
print(e * 2)
while printed >= 0:
    printed -= 1
    print(printed)

string = 'my string'
summa = 0
for elem in string:
    summa += pow(string.find(elem), 2)
    print("sum =", summa)


def my_func(atr=1):
    print('atr: ', atr)


my_func(atr=5)