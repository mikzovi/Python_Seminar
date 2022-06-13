# 2 - Реализовать RLE алгоритм. реализовать модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных файлах 
# (в одном файлике отрывок из какой-то книги, а втором файлике — сжатая версия этого текста). 

filename_in = 'Task_S06_02_data.txt'
filename_out = 'Task_S06_02_encode_data.txt'
filename_or = 'Task_S06_02_decode_data.txt'

#Функция простого отображения оригинального текста в файле, ну для себя и проверки
def orig_text(file):
    with open(file,'r') as f:
        for i in f:
            txt = ''.join(str(i)) 
    return(txt)   

# Просто нашел алгоритм как он работает и по правилам описал здесь
def encode_text(file_in,file_out):
    with open(file_in,'r') as f:
        for i in f:
            txt = ''.join(str(i))
    enc_str = ""
    i = 0
    while (i <= len(txt)-1):
        count = 1
        ch = txt[i]
        j = i
        while (j < len(txt)-1):  
            if (txt[j] == txt[j + 1]): 
                count += 1
                j += 1
            else: 
                break
        enc_str += str(count) + ch
        i = j + 1
    with open(file_out,'w') as f:
        f.write(enc_str) 
    return enc_str # Вывод в консоль - просто что б видеть

# Разжатие по правилам
def decode_text(file_out,file_r):
    with open(file_out,'r') as f:
        for i in f:
            txt = ''.join(str(i))    
    dec_str = ""
    i = 0
    j = 0
    while (i <= len(txt) - 1):
        count = int(txt[i])
        word = txt[i + 1]
        for j in range(count):
            dec_str += word
            j = j + 1
        i = i + 2
    with open(file_r,'w') as f:
        f.write(dec_str)
    return dec_str # Вывод в консоль - просто что б видеть

print(f'Оригинальный текст: \n {orig_text(filename_in)}')
print('')
print(f'Сжатый текст: \n {encode_text(filename_in,filename_out)}')
print('')
print(f'Вернули текст: \n {decode_text(filename_out,filename_or)}')
print('')