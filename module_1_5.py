immutable_var = (2, 4, 6, 8, True, 'float', 'Food')
print(immutable_var)
immutable_var[4] = False
print(immutable_var[4]) # значения элементов кортежа изменить нельзя, поскольку кортеж неизменяем в отличие от списка, в котором возможно заменить значения элементов
mutable_list = [1, 3, 5, False, 'string']
print(mutable_list)
mutable_list[4] = 'float'
mutable_list[3] = True
print(mutable_list)


