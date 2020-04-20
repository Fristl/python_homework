"""Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль."""

def my_func(var_1, var_2):
    try:
        result = var_1 / var_2
        return result
    except ZeroDivisionError:
        return f'На ноль делить нельзя!'

my_list = []
i = 0

while i != 2:
    var = input('Введите целое положительное число: ')
    if var.isdigit():
        var = int(var)
        my_list.insert(i, var)
        i += 1
    else:
        print('Ошибка ввода, введите только целое число')

print(my_func(my_list[0], my_list[1]))
