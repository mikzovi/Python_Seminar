# 4. Дана последовательность чисел. Получить список неповторяющихся элементов исходной последовательности
# Пример: [1, 2, 3, 5, 1, 5, 3, 10] => [1, 2, 3, 5, 10]

def find_unique_elements(current_list):
    unique_list = []
    for item in current_list:
        if not item in unique_list:
            unique_list.append(item)
    return unique_list

original_list = [1, 2, 3, 5, 1, 5, 3, 10]  
print(f'Исходная последовательность чисел: {original_list}')
print(f'Список неповторяющихся элементов исходной последовательности: {find_unique_elements(original_list)}')
