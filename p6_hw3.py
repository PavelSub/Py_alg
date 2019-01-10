# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

list_1 = [8, 3, 15, 6, 6, 4, 2]
min_i, max_i, min_p, max_p, j = list_1[0], list_1[0], 0, 0, 0
for i in list_1:
    if i > max_i:
        max_i = i
        max_p = j
    if i < min_i:
        min_i = i
        min_p = j
    j += 1

if max_p < min_p:
    max_p, min_p = min_p, max_p

sum_i = 0
for i in range(min_p + 1, max_p):
   sum_i = list_1[i] + sum_i

print(sum_i)
