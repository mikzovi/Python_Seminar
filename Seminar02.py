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

def in_spisok(chislo, spisok):
    for i in spisok:
        if str(chislo) in i:
            return True
    return False

spissok = ['geek', 'brains4', '5five', '3friends']
chislo = 4

print(in_spisok(4, spissok))
print(in_spisok(2, spissok))