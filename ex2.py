"""Реализовать функцию, принимающую несколько параметров,
описывающих данные пользователя: имя, фамилия, год рождения,
город проживания, email, телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой."""

my_list = []
my_list_2 = [
    'Имя: ', 'Фамилия: ', 'Год рождения: ',
    'Город проживания: ', 'Email: ', 'Номер телефона: '
]

for q in my_list_2:
    var = input(f'Введите {q}')
    my_list.append(var)

def info(
        name=my_list[0], surname=my_list[1],
        year_of_birth=my_list[2], city=my_list[3],
        email=my_list[4], tel=my_list[5]):
    return f'{my_list_2[0]}{name}, {my_list_2[1]}{surname}, ' \
           f'{my_list_2[2]}{year_of_birth}, {my_list_2[3]}{city}, ' \
           f'{my_list_2[4]}{email}, {my_list_2[5]}{tel}'

print(info())

def info_2(name='Владислав', surname='Рубан',
        year_of_birth=1996, city='Москва',
        email='почта', tel=96321):
    return f'{my_list_2[0]}{name}, {my_list_2[1]}{surname}, ' \
           f'{my_list_2[2]}{year_of_birth}, {my_list_2[3]}{city}, ' \
           f'{my_list_2[4]}{email}, {my_list_2[5]}{tel}'
print(info_2())
