# Задача 01
# Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

def sequence(k):
    result = []
    for i in range(0, k):
        result.append((-3)**i)
    return(result)

n=5
print(f'Cписок из {n} членов последовательности (-3)**n :')
print(sequence(n))

