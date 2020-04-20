"""Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов."""

def my_func(x, y, z):
    if x >= y:
        max_1 = x
        if y >= z:
            max_2 = y
        else:
            max_2 = z
    elif x >= z:
        max_1 = x
        if y >= z:
            max_2 = y
        else:
            max_2 = z
    else:
        max_1 = y
        max_2 = z
    result = max_1 + max_2
    print(max_1, max_2)
    return result

i = 0
while i != 3:
    var = input('Введите целое положительное число: ')
    if var.isdigit():
        var = int(var)
        i += 1
    else:
        print('Ошибка ввода, введите только целое число')

print(my_func(my_list[0], my_list[1], my_list[2]))
