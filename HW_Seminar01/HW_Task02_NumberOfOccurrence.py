# Задача 02
# Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.
# 'Говорил попугай попугаю: Я тебя, попугай, попугаю. Отвечает ему попугай: Попугай, попугай, попугай!'

# попугаю:' # Я тебя, попугай, попугаю. Отвечает ему попугай: Попугай, попугай, попугай!'
text = 'Говорил попугай попугаю: Я тебя, попугай, попугаю. Отвечает ему попугай: Попугай, попугай, попугай!'
element = 'поп'


def number_of_occurence(current_text, current_element):
    count = 0
    i = 0
    lower_current_text = current_text.lower()
    lower_current_element = current_element.lower()

    len_current_text = len(current_text)
    len_current_element = len(current_element)

    while i < (len_current_text - len_current_element + 1):
        if lower_current_element == lower_current_text[i:i+len_current_element]:
            count += 1
            i = i + len_current_element
        else:
            i += 1
    return count

print(f'Количество вхождений елемента "{element}" в строке \n"{text}": \n{number_of_occurence(text, element)}')


