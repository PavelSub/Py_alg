# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на
# промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована
# в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random


def bubble_sort(arr):
    n, not_sort = 1, True
    while not_sort:
        not_sort = False
        for i in range(len(arr) - n):
            if arr[i] < arr[i + 1]:
                arr[i + 1], arr[i], not_sort = arr[i], arr[i + 1], True
        n += 1


r_arr = [random.randint(-100, 100) for i in range(25)]

print(f'Не сортированный: {r_arr}')
print(f'Сортированный: {bubble_sort(r_arr)}')
