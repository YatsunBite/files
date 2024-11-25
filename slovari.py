phone_book = {'Nastia': 89652757655, 'Kom': 89191917555} # словарь - неупорядоченная коллекция
print(phone_book)
print(phone_book['Kom'])
phone_book['Kom'] = 8987654333
print(phone_book)
phone_book['Nazar'] = 8976545789980
print(phone_book)
del phone_book['Nastia']
print(phone_book)
phone_book.update({'Sania':89760000998, 'Alex': 123432321})
print(phone_book)
print(phone_book.get('Kom'))
print(phone_book.get('Roma'))
print(phone_book.get('Roma', 'такого ключа нет'))
phone_book.pop('Nazar')
print(phone_book)
a = phone_book.pop('Sania')
print(a)
print(phone_book.keys())
print(phone_book.values())
print(phone_book.items())
