Знакомство с Python 
Домашнее задание к семинару 03

1. Найти НОК двух чисел
2. Вычислить число Пи c заданной точностью d
Пример: при d = 0.001,  c= 3.141. 
3. Составить список простых множителей натурального числа N

4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

+ на тему файловой системы:
5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа. 


Экстра-задачи:
1. Определите функцию, которая принимает римскую цифру в качестве аргумента и возвращает ее значение в виде числового десятичного целого числа. Вам не нужно проверять форму римской цифры.
Современные римские цифры записываются путем выражения каждой десятичной цифры числа, которое должно быть закодировано отдельно, начиная с самой левой цифры. Таким образом, 1990 отображается "MCMXC" (1000 = M, 900 = CM, 90 = XC), а 2008 отображается "MMVIII" (2000 = MM, 8 = VIII). Римская цифра для 1666, "MDCLXVI", использует каждую букву в порядке убывания.
Пример: имя_вашей_функции ('XXI') # должно вернуть 21

2. Определите функцию, которая удаляет весь текст, следующий за любым из переданных маркеров комментариев. Любые пробелы в конце строки также должны быть удалены.
Пример: 
Входные данные:
«apples, pears # and bananas
grapes
bananas !apples          » 
Выходные данные:
«apples, pears
grapes
bananas»
Функция может вызываться вот так:
result = function("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])

3. Начиная в вершине треугольника (см. пример ниже) и перемещаясь вниз на смежные числа, максимальная сумма до основания составляет 23.
3
7 4
2 4 6
8 5 9 3
То есть, 3 + 7 + 4 + 9 = 23.
Найдите максимальную сумму пути от вершины до основания следующего треугольника:
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

4. Сумма квадратов первых десяти натуральных чисел равна
1^2 + 2^2 + ... + 10^2 = 385
Квадрат суммы первых десяти натуральных чисел равен
(1 + 2 + ... + 10)2 = 552 = 3025
Следовательно, разность между суммой квадратов и квадратом суммы первых десяти натуральных чисел составляет 3025 − 385 = 2640.
Найдите разность между суммой квадратов и квадратом суммы первых ста натуральных чисел.