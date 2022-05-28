# 1.	Найти сумму чисел списка стоящих на нечетной позиции
# Пример:[1,2,3,4] -> 4

spisok = [1,2,3,4]

def sum_odd_index(current_list):
    length_current_list = len(current_list)
    sum = 0
    for i in range(0,length_current_list,2):
        sum += current_list[i]
    return sum

print(f'Сумма чисел списка {spisok}, стоящих на нечетной позиции: {sum_odd_index(spisok)}')

