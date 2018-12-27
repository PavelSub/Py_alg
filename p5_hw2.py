# 5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

def print_ascii(st, end, cl):
    s, f, line = st, end, ''
    while s <= f:
        for i in range(cl):
            point = s + i
            if point > end:
                break
            else:
                line = line + f'{point} - {chr(point)} '
        print(line)
        line = ''
        s += cl


print_ascii(32, 127, 10)
