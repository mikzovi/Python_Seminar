# 5.  Дан текстовый файл, содержащий целые числа. Удалить из него все четные числа.

import random


def int_number_list(file_in):
    n = 10
    with open(file_in, 'w') as file:
        for i in range(n):
            file.write(str(random.randint(1, n-1)) + '\n')
    return


def odd_numbers_list(file_in, file_out):
    collection_odd = []
    with open(file_in, 'r') as file:
        for i in file:
            if int(i) % 2 != 0:
                collection_odd.append(str(i))
        with open(file_out, 'w') as file:
            for i in collection_odd:
                file.write(str(i))
        return


int_number_list('Task_S03_05_in.txt')
odd_numbers_list('Task_S03_05_in.txt', 'Task_S03_05_out.txt')

with open('Task_S03_05_in.txt', 'r') as file:
    print('Содержимое входного файла: ')
    for i in file:
        print(str(int(i)))

with open('Task_S03_05_out.txt', 'r') as file:
    print('Содержимое выходного файла: ')
    for i in file:
        print(str(int(i)))
