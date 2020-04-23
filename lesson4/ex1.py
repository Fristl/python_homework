"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами."""

import sys

if len(sys.argv) >= 4:
    param = [i for i in sys.argv[1:4]]
else:
    print('Вы ввели недостаточно данных!\nПовторите выполнение программы сначала.')
    exit()

for spam, q in enumerate(param):
    if q.isdigit():
        param[spam] = int(q)
    else:
        print(f'Вы ошиблись при вводе {spam+1}-го параметра.\n'
              f'Повторите выполнение программы сначала.\n'
              f'Вводите в качестве параметров только целые неотрицательные числа.')
        exit()

def my_func(production_in_hours, rate_per_hour, premium):
    salary = (production_in_hours * rate_per_hour) + premium
    return salary

print(my_func(param[0], param[1], param[2]))
