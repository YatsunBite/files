food = ['apple','coconut','banana']
food.append(True)
print(food)
food.extend(['string', 2])
print(food)
food.remove('apple')
print(food)
print('coconut' not in food)
print(food[0:2])
food[0] = 'peach'
print(food[0])