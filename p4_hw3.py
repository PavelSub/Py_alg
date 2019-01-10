# 4. Определить, какое число в массиве встречается чаще всего.

list_1, max_freq, max_num = [8, 3, 3, 3, 3, 15, 6, 4, 4, 4, 4, 4, 4, 2, 2, 2], 0, 0

for i in set(list_1):
    k = 0
    for j in list_1:
        if i == j:
            k += 1
    if k > max_freq:
        max_freq = k
        max_num = i

print(max_num)
