tuple_ = 1, 2, 3, True, 'String' # кортеж - неизменяемая упорядоченная коллекция разных типов данных
tuple_2 = (1, 2, 3, 4)
tuple_3 = tuple([1, 2, 3, 4])
print(tuple_)
print(tuple_2)
print(tuple_3)
print(type(tuple_))
print(tuple_[0]) # tuple_[0] = 100 - ошибка, поскольку в кортеже объекты неизменяемы!
list_ = 1, 2, 3, True, 'String'
print(tuple_.__sizeof__()) # команда, отражающая размер памяти
print(list_.__sizeof__())
tuple_4 = ([1, 2], 0)
print(tuple_4)
tuple_4[0][0] = 2
print(tuple_4)
tuple_5 = (1, 3, 5) + (2, 4)
print(tuple_5)
tuple_6 = (1, 2) * 3
print(tuple_6)
