"""Представлен список чисел. Необходимо вывести элементы исходного списка,
значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию,оформить в виде списка.
Для формирования списка использовать генератор."""

my_list = [
    1, 2, 5, 152,
    13, 15, 3, 1,
    1, 3, 5, 18,
    -10, -5, 34, 22
]

def my_func(some_list):
    for i, spam in enumerate(some_list):
        if i == 0:
            yield spam
            continue
        elif spam > some_list[i-1]:
            yield spam

result = [my_func(my_list)]

print(result)
print(list(my_func(my_list)))
print('__________________________________________________________')

answ = [item for q, item in enumerate(my_list) if (item > my_list[q-1] or q == 0)]
print(answ)
