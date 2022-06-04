# 1.	Создать и заполнить файл случайными целыми значениями.
# Выполнить сортировку содержимого файла по возрастанию.

import os
from random import randint
path = 'HW_Seminar04/'
rand_int_file = 'rand_int_file.txt'
randint_file_fullpath = os.path.join(path, rand_int_file)

sort_int_file = 'sort_int_file.txt'
sort_file_fullpath = os.path.join(path, sort_int_file)

rand_int_list = [randint(0, 20) for _ in range(randint(0, 20))]

print(rand_int_list)

with open(randint_file_fullpath, 'w') as f:
    f.write("\n".join(map(str, rand_int_list)))

sorted_int_list = []

with open(randint_file_fullpath, 'r') as f:
    sorted_int_list = list(map(int, f.readlines()))
    sorted_int_list.sort()

with open(sort_file_fullpath, 'w') as f:
    f.write("\n".join(map(str, sorted_int_list)))

print(sorted_int_list)
