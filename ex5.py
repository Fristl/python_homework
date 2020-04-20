"""Программа запрашивает у пользователя строку чисел, разделенных пробелом.
При нажатии Enter должна выводиться сумма чисел.
Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
Но если вместо числа вводится специальный символ, выполнение программы завершается.
Если специальный символ введен после нескольких чисел,
то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу."""

def my_func():
    itm = True
    result = 0
    while itm:
        my_list = []
        numbers = input('Введите целые неотрицательные числа через пробел (Для завершения введите q): ')
        numbers = numbers.split(' ')
        for i, spam in enumerate(numbers):
            if spam.isdigit():
                numbers[i] = int(spam)
                my_list.append(numbers[i])
            elif spam == 'q':
                itm = False
            else:
                while True:
                    numbers[i] = input(f'Ошибка ввода {i+1}-го элемента.\nВведите только целое неотрицательное число: ')
                    if numbers[i].isdigit():
                        numbers[i] = int(numbers[i])
                        my_list.append(numbers[i])
                        break

        for eggs in my_list:
            result += eggs
        print(result)
    return result

my_func()
