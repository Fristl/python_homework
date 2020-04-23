"""Реализовать два небольших скрипта:
а) итератор, генерирующий целые числа, начиная с указанного,
б) итератор, повторяющий элементы некоторого списка, определенного заранее.
Подсказка: использовать функцию count() и cycle() модуля itertools.
Обратите внимание, что создаваемый цикл не должен быть бесконечным.
Необходимо предусмотреть условие его завершения.
Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено."""

import sys
import time
from itertools import (
    count,
    cycle
)

_, itm = sys.argv
my_list = []

for el in count(int(itm)):
    if el > 20:
        break
    else:
        print(el)
        my_list.append(el * 2)

print('\n\n')

с = 0
for el in cycle(my_list):
    if с > 3 * len(my_list):
        break
    print(el)
    time.sleep(0.2)
    с += 1
