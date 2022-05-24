# Задача 03
# Подсчитать сумму цифр в вещественном числе.

def sum_of_digits(current_number):
    sum = 0
    for i in str(current_number):
        if i.isdigit():
            sum += int(i)
    return sum

number = float(input("Введите вещественное число: "))
print(f"Сумма всех чисел в вещественном чиле {number} = {sum_of_digits(number)}")