
# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.

def sum_l(n):
    j = 1
    for i in range(n):
        if i == 0:
            pass
        elif i%2 != 0:
            j = j + (j/2 * (-1))
        else:
            j = j + j/2
    return j


print(sum_l(int(input('Введите длину ряда: '))))
