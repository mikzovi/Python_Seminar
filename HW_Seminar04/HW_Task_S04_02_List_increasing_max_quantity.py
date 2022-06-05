# 2.	Дан список чисел. Создать список в который попадают числа,
# описывающие возрастающую последовательность
# и содержащие максимальное количество элементов.
# Пример: [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3, 4, 6, 7]
#  [5, 2, 3, 4, 6, 1, 7] => [2, 3, 4, 6, 7]
#  Порядок элементов менять нельзя

# Разберите, пожалуйста, подробно решение этой задачи на семинаре. И условие тоже. 
# Моя поделка отрабатывает, но не для всех списков корректно. Что-то явно не так. 
# Двое суток решать одну задачу - непозволительная для меня роскошь. 
# Разбирайте, пожалуйста, реально работающий код всех домашних задач на семинарах.
# Пользы от этого будет реально больше. 

def list_increas_sequence(current_list):
    list_increas = [0] * len(current_list)
    for i in range(len(current_list)):
        list_increas[i] = []

    list_increas_enique = []
    temp_list = []

    for i in range(len(current_list)-1):
        list_increas[i].append(current_list[i])
        k = i+1
        while True:
            for j in range(k, len(current_list)):
                if current_list[j] > list_increas[i][-1]:
                    temp_list.append(current_list[j])

            if len(temp_list) == 0:
                break

            if max(temp_list) == temp_list[0]:
                list_increas[i].append(temp_list[0])
            else:
                list_increas[i].append(min(temp_list))
            temp_list = []
            k += 1

            if list_increas[i] not in list_increas_enique and len(list_increas[i]) > 1:
                list_increas_enique.append(list_increas[i])
    return list_increas_enique


#list_numbers = [5, 2, 3, 4, 6, 1, 7]
list_numbers = [1, 5, 2, 3, 4, 6, 1, 7]
#list_numbers = [1, 5, 4, 2, 3, 4, 1]
#list_numbers = [5, 4, 3, 2, 1]


print('----------------------------')
print(f'Дан список чисел: {list_numbers}')

list_increas_numbers = list_increas_sequence(list_numbers)

print('Возрастающие последовательности в заданном списке:')
if len(list_increas_numbers) != 0:
    for i in range(len(list_increas_numbers)):
        print(list_increas_numbers[i])
else:
    print('не найдены')

print('Возрастающая последовательность c максимальным количеством элементов:')
if len(list_increas_numbers) != 0:
    list_increas_max = list_increas_numbers[0]
    for i in range(len(list_increas_numbers)):
        if len(list_increas_max) < len(list_increas_numbers[i]):
            list_increas_max = list_increas_numbers[i]
    print(list_increas_max)
else:
    print('не найдена')
print('----------------------------')
