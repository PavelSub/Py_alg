# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на
# промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random


def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    if not len(left) or not len(right):
        return left or right

    res, i, j = [], 0, 0

    while len(res) < len(left) + len(right):
        if left[i] < right[j]:
            res.append(left[i])
            i += 1
        else:
            res.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            res.extend(left[i:] or right[j:])
            break
    return res


r_arr = [random.randint(0, 50) for i in range(25)]


print(f'Не сортированный: {r_arr}')
print(f'Сортированный: {merge_sort(r_arr)}')
