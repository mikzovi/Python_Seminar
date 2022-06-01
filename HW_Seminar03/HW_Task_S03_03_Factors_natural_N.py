# 3. Составить список простых множителей натурального числа N

def list_prime_multipliers(current_number):
    list_prime = []
    devider = 2
    while current_number > 0 and devider <= current_number:
        if current_number % devider == 0:
            list_prime.append(devider)
            current_number = current_number / devider
        else:
            devider +=1
    return list_prime

number = int(input("Введите натуральное число: "))
print(f"Список простых множителей натурального числа {number}: {list_prime_multipliers(number)}")