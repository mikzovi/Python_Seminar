# Задача 04
# Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

def factorial(n):
    return 1 if n == 0 else n * factorial(n-1)

print([factorial(i) for i in range(1, int(input("Введите N: "))+1)])
