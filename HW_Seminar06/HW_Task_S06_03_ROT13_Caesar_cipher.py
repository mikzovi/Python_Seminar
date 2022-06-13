# 3 -  ROT13 - это простой шифр подстановки букв, который заменяет букву буквой, 
# которая идет через 13 букв после нее в алфавите. 
# ROT13 является примером шифра Цезаря.
# Создайте функцию, которая принимает строку и возвращает строку, зашифрованную с помощью Rot13 . 
# Если в строку включены числа или специальные символы, они должны быть возвращены как есть. 
# Также создайте функцию, которая расшифровывает эту строку обратно (некий начальный аналог шифрования сообщений). 
# Не использовать функцию encode.

alphabet_eng = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def rot13_encoding(text: str) -> str:  # encoding ROT13
    return cesar_encoding(text, 13)


def rot13_decoding(text: str) -> str:  # decoding ROT13
    return cesar_encoding(text, -13)


def cesar_encoding(text: str, key: int) -> str:  # aux cesar method
    result = ''

    for ch in text.upper():
        if ch in alphabet_eng:
            result += alphabet_eng[(alphabet_eng.find(ch) + key) % len(alphabet_eng)]
        else:
            result += ch

    return result


print(cesar_encoding('13 & Why are you going to go there?..', 13))

print(rot13_encoding('13 & Why are you going to go there?..'))

print(rot13_decoding(rot13_encoding('13 & Why are you going to go there?..')))
