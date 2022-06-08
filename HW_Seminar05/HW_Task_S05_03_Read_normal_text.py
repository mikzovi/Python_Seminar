# 3. Вот вам текст:
# «Ну, вышел я, короче, из подъезда. В общем, короче говоря, шел я, кажется, в магазин. 
# Ну,эээ, в общем, было лето, кажется. Как бы тепло. Солнечно, короче. 
# Иду я, иду, в общем, по улице, а тут, короче, яма. Я, эээээ…. Упал в нее. 
# И снова вышел, короче, из подъезда. Ясен пень, в магазин. 
# В общем, лето на дворе, жарко, солнечно, птицы, короче, летают. 
# Кстати, иду я по улице, иду, а тут, короче, яма. Ну, я в нее упал, в общем. 
# Вышел из подъезда, короче. Лето на дворе, ясен пень. Птицы поют, короче, солнечно. В общем, в магазин мне надо. 
# Что-то явно не так, короче. «Рекурсия», - подумал я. Ээээ...короче, в общем, пошел другой дорогой и не упал в эту… ээээ… яму. Хлеба купил».
# 
# Отфильтруйте его, чтобы этот текст можно было нормально прочесть. 
# Предусмотрите вариант, что мусорные слова могли быть написаны без использования запятых.

import os

#def filter_text(file_path: str) -> None:
def filter_text(origin_text, read_normal_text):
    junk_words = ['короче говоря', 'короче', 'кстати', 'эээээ', 'ээээ', 'эээ', 'кажется', 'ясен пень', 'в общем', 'ну', 'как бы']

    with open(origin_text, "r", encoding='utf-8') as file:
        text = file.read().lower()
        #print(test_line)
        for junk_word in junk_words:
            text = text.replace(', ' + junk_word + '...', '')
        for junk_word in junk_words:
            text = text.replace(', ' + junk_word, '')
        for junk_word in junk_words:
            text = text.replace(junk_word + ', ', '')
        for junk_word in junk_words:
            text = text.replace(junk_word + '...', '')
        for junk_word in junk_words:
            text = text.replace(' ' + junk_word, '')
        for junk_word in junk_words:
            text = text.replace(junk_word, '')

    while text[1] == ',' or text[1] == ' ' or text[1] == '...':
        text = text[1:]

    with open(read_normal_text, "w", encoding='utf-8') as file:
        file.write(text)


path = 'HW_Seminar05/'
origin_file = 'HW_Task_S05_03_Original_text.txt'
read_normal_file = 'HW_Task_S05_03_Read_normal_text.txt'
origin_text = os.path.join(path, origin_file)
read_normal_text = os.path.join(path, read_normal_file)

filter_text(origin_text, read_normal_text)

with open(origin_text, "r", encoding='utf-8') as f:
    for line in f:
        print (line.strip())
print('##############################')
with open(read_normal_text, "r", encoding='utf-8') as f:
    for line in f:
        print (line.strip())
