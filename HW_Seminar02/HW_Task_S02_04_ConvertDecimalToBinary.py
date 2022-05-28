# 4.	Написать программу преобразования десятичного числа в двоичное

def decimal_to_binar(current_num):
    binar_num = ''
    while current_num > 0:
        binar_num = str(current_num % 2) + binar_num
        current_num = current_num // 2
    return binar_num


#num = 1653
num = int(input('Введите десятичное число: '))
print(f'Десятичное число {num} в двоичном выражении: {decimal_to_binar(num)}')
