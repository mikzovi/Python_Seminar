# Задача 1. Реализуйте алгоритм перемешивания списка.

# Задача 2. Реализовать алгоритм задания случайного числа без генератора случайных чисел

# Задача 3. Задайте список из n чисел последовательности (1+1.n)**n и выведите на экран их сумму.

# Задача 4. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число
# ['geek', 'brains4', '5five', 3friends']


# Задача 2.

# import time


# def random(min, max):
#     rnd = time.time()
#     rnd = rnd - int(rnd)
#     rnd = int(rnd * (max-min+1) + min)
#     return rnd

# print (random(50, 60))


# Задача 1. Реализуйте алгоритм перемешивания списка.


# spisok = [1, 4, 90, 'sadf', True, 'rrr', False]
# size = len(spisok)
# new_spisok = []
# print(spisok)
# while size > 0:
#     index = random(0, size - 1)
#     new_spisok.append(spisok[index])
#     spisok.pop(index)
#     size -= 1

# print(new_spisok)


# Задача 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

# n = 15
# posl = []
# sum = 0
# for i in range(1, n+1):
#     posl.append((1 + 1/i)**i)
#     sum += posl[i-1]

# print(posl)
# print(sum)


# Задача 4. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число
# ['geek', 'brains4', '5five', 3friends']

# def in_spisok(chislo, spisok):
#     for i in spisok:
#         if str(chislo) in i:
#             return True
#     return False

# spissok = ['geek', 'brains4', '5five', '3friends']
# chislo = 4

# for i in range (0, 20):
#     print(f'Число {i} {in_spisok(i, spissok)}')


# 2520 - самое маленькое число, которое делится без остатка на все числа от 1 до 10.
# Какое самое маленькое число делится нацело на все числа от 1 до 20?

def Delitsyali(n):
    for i in range(1,11):
        if n % i != 0:
            return False
    return True

x = 20
b = False
while not b:
    x += 10
    b = Delitsyali(x)
    print(f'{x} {b}')
print(x)
