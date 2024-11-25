name = input('введите имя: ')
current_year = 2024
date_of_birth = int(input('В каком году вы родились? '))
age = current_year - date_of_birth # команду int можно вставить и при вычислении
print('Здравствуйте,', name)
print('В этом году вам', age, 'года')
print('привет, я строка в верхнем регистре'.upper())
print('привет, я строка в нижнем регистре'.lower())
print('привет, я строка в нижнем регистре'.replace('привет', 'пока'))