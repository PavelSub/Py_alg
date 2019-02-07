# 3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше
# медианы, в другой – не больше медианы. Задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках

import random


def median_f_by_min(arr):
    c_arr = arr.copy()
    mid = round((len(c_arr) + 0.5) / 2)
    pos = 0
    m_arr = []
    while pos < mid:
        min_el = min(c_arr)
        m_arr.append(min_el)
        c_arr.remove(min_el)
        pos += 1
    if len(arr) % 2 == 0:
        return (m_arr[-1] + min(c_arr)) / 2
    else:
        return m_arr[-1]


def median_f_by_sel(arr):
    mid = len(arr) // 2
    for i in range(mid + 2):
        ind_m = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[ind_m]:
                ind_m = j
        arr[i], arr[ind_m] = arr[ind_m], arr[i]
    if len(arr) % 2 == 0:
        return (arr[mid] + arr[mid - 1]) / 2
    else:
        return arr[mid]


arr = [random.randint(0, 100) for i in range(2 * random.randint(0, 50) + 1)]


print(f'Массив: {arr}')
print(f'Медиана: {median_f_by_min(arr)}')
print(f'Медиана: {median_f_by_sel(arr)}')
