# 1. Найти НОК двух чисел

number_x = int(input("Введите первое число: "))
number_y = int(input("Введите второе число: "))


def nok_calculate(current_number_x, current_number_y):
    if current_number_x > current_number_y:
        bigger_number = current_number_x
    else:
        bigger_number = current_number_y
    while(True):
        if (bigger_number % current_number_x == 0) and (bigger_number % current_number_y == 0):
            nok = bigger_number
            break
        bigger_number += 1
    return nok

print(
    f"Наименьшее общее кратное чисел {number_x} и {number_y}: {nok_calculate(number_x,number_y)}")
