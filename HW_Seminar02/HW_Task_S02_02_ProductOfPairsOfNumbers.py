# 2.	Найти произведение пар чисел в списке.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример: [2, 3, 4, 5, 6] => [12, 15, 16]; [2, 3, 5, 6] => [12, 15]

origin_list = [2, 3, 4, 5, 6]


def product_of_pairs(current_list):
    num_pairs = len(current_list)//2 + len(current_list) % 2
    product_list = []
    for i in range(0, num_pairs):
        product_list.append(current_list[i] * current_list[-(i+1)])
    return product_list

print(f'Входной список: {origin_list}')
print(f'Список произведений пар чисел входного списка: {product_of_pairs(origin_list)}')
