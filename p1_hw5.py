'''
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
 Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
'''

import collections as col

comp_count, comp_titles, comp_rev, C_rev, tot_rev = int(input('Введите количество предприятий: ')), [], [], col.namedtuple('C_rev', ['title', 'q_1', 'q_2', 'q_3', 'q_4', 'total']), 0

for i in range(comp_count):
	comp_titles.append(str(input('Введите название компании: ')))

for i in comp_titles:
	print(f'Введите прибыль для компании {i}: ')
	r_1, r_2, r_3, r_4 = int(input('За 1 квартал: ')), int(input('За 2 квартал: ')), int(input('За 3 квартал: ')), int(input('За 4 квартал: '))
	comp = C_rev(i, r_1, r_2, r_3, r_4, r_1 + r_2 + r_3 + r_4)
	comp_rev.append(comp)
	tot_rev += comp.total

avr_rev, b_avr, a_avr = tot_rev / comp_count, [], []

for i in comp_rev:
	b_avr.append(i) if i.total < avr_rev else a_avr.append(i)

print(f'Средняя прибыль предприятий за год составила {avr_rev} $', sep = '/n')
print('Компании прибыль которых превысила среднее значение: ')
[print(f'{i.title} - {i.total} $', sep = '/n') for i in a_avr]
print('Компании прибыль которых не достигла среднего значения: ')
[print(f'{i.title} - {i.total} $', sep = '/n') for i in b_avr]

