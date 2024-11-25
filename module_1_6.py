my_dict={'I':2002, 'Nazar':2006, 'Mama':1980, 'Papa':1952}
print(my_dict)
print(my_dict['Mama'])
my_dict['Bonia']=2020
print(my_dict)
my_dict.update({'Ser':2003,'Bysia':2018})
print(my_dict)
del my_dict['I']
print(my_dict)

my_set={1, 1, 2, 2, 4, 4, 6, 6, 9, 9, 'i', (9, 9)}
print(my_set)
print(my_set.add(10))
print(my_set.add('float'))
print(my_set)
print(my_set.discard(4))
print(my_set)