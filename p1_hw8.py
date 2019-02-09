# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N,
# состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
import hashlib
import random


def substring_f(string):
    i, j = 0, 1
    l_hash = [hashlib.sha1(string.encode('utf-8')).hexdigest()]
    len_str = len(string)
    while i < len_str:
        while j <= len_str:
            h_res = hashlib.sha1(string[i:j].encode('utf-8')).hexdigest()
            if h_res not in l_hash:
               l_hash.append(h_res)
            j += 1
        i += 1
        j = i + 1
    return l_hash


m = int(input('Введите длину строки: '))
s_srt = ''.join([chr(random.randint(97, 122)) for i in range(m)])
print(f'Количество подстрок в строке {s_srt} - {len(substring_f(s_srt)) - 1}')
