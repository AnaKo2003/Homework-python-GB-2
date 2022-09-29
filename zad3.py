"""Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму."""

n = int(input('Введите число: '))
list = []
for i in range(1, n + 1):
    list.append(round(float((1 + 1 / i) ** i), 2))
print(f'При k = {n} числа последовательности (1+1\k)^k: {list}')
sum = 0
for j in range(len(list)):
    sum += list[j]
print(f'Cумма чисел последовательности = {sum}')