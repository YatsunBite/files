from tkinter.scrolledtext import example

name = 'Nastia'
print('Hello, '+ name)
print('Hello, ''Nastia')
print('Hello'*5)
print(name[0]) # выделение элемента (символа) из строки (отсчет элементов начинается ВСЕГДА с 0!!)
print(name[-1])
print(name[0:3]) # двоеточие - 0, 1, 2 - от нуля до трех, но последний номер не включается
print(name[0:3:2]) # от нуля до 3го символа невключительно, НО с ШАГОМ в 2 символа
print(name[:3]) # без начала (но с начала - с первого символа) можно не указывать начальный символ, а лишь конечный
print(name[2:]) # так же и наоборот - можно указать от определенного символа до конца
print(name[::-1])

example = 'Топинамбур'
print(example[0])
print(example[-1])
print(example[5:])
print(example[::-1])
print(example[1::2])