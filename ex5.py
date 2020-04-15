"""Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
У пользователя необходимо запрашивать новый элемент рейтинга.
Если в рейтинге существуют элементы с одинаковыми значениями,
то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]."""

my_list = [10, 6, 5, 5, 4, 2, 2, 1]
print(my_list)
while True:
    number = input('Введите целое неотрицательное число (для завершения введите q): ')
    if number.isdigit():
        number = int(number)
        my_list.reverse()
        if number in my_list:
            var = my_list.index(number)
            my_list.insert(var, number)
        else:
            i = -1
            for itm in my_list:
                i += 1
                if number < itm:
                    my_list.insert(i, number)
                    break
                elif my_list[i + 1] > number > itm:
                    my_list.insert(i + 1, number)
                    break
                elif number > my_list[-1]:
                    my_list.insert(len(my_list), number)
                    break
                else:
                    continue
        my_list.reverse()
        print(my_list)
    elif number == 'q':
        break
    else:
        print('Ошибка ввода, введите только неотрицательное целое число')
