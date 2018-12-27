# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

def maxint(m, i):
    si = 0
    for j in i:
        si += int(j)
    return {'max_i': i, 'max_sum': si} if si > m['max_sum'] else m


m_i = {'max_i': 0, 'max_sum': 0}

while True:
    ans = input('Добавить число или прервать?(Y/N): ')
    if ans == 'Y' or ans == 'y':
        m_i = maxint(m_i, input('Введите натуральное число: '))
    else:
        print(f"Наибольшее число - {m_i['max_i']}, сумма цифр {m_i['max_sum']}")
        break

