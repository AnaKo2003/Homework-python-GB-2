"""Реализуйте алгоритм перемешивания списка."""

import random
list = []
for i in range(10):
    list.append(random.randint(-5, 5))
print(f'Первоначальный список: {list}')
random.shuffle(list)
print(f'Перемешанный список: {list}')