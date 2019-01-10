# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

list_1 = [8, 3, 15, 6, 4, 2]
min_i, max_i, min_p, max_p, j = list_1[0], list_1[0], 0, 0, 0
for i in list_1:
    if i > max_i:
        max_i = i
        max_p = j
    if i < min_i:
        min_i = i
        min_p = j
    j += 1

list_1[min_p], list_1[max_p] = list_1[max_p], list_1[min_p]

print(list_1)
