# 3.	В заданном списке вещественных чисел найдите разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример: [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

origin_list = [1.1, 1.2, 3.1, 5, 10.01]

def difference_fractional_part(current_list):
    temp_list = [current_list[i] - math.trunc(current_list[i]) for i in range(0, len(current_list))]
    return max(temp_list)-min(temp_list)


print(f'Входной список: {origin_list}')

print(f'Разница между максимальным и минимальным значениями дробной части элементов входного списка равна: {difference_fractional_part(origin_list)}')
