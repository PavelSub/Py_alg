# 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# python -m timeit -n 100 -s "import hw4" "hw4.min_by_sort(hw4.rand_arr)"

import random
import cProfile
# import timeit

size = 10000

rand_arr = [random.randint(size * -10, size * 10) for _ in range(size)]

# python -m timeit -n 100 "import p1_hw4" "p1_hw4.min_by_sort(p1_hw4.rand_arr)"

def min_by_sort(list_1, c=2):
    list_1.sort()
    return list_1[:c]

# cProfile.run('min_by_sort(rand_arr, 2)')
'''
###size = 10000

100 loops, best of 5: 127 usec per loop

5 function calls in 0.001 seconds
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
     1    0.000    0.000    0.001    0.001 <string>:1(<module>)
     1    0.000    0.000    0.001    0.001 hw4.py:14(min_by_sort)
     1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
     1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
     1    0.001    0.001    0.001    0.001 {method 'sort' of 'list' objects}

###size = 100000
100 loops, best of 5: 1.58 msec per loop

###size = 1000000

100 loops, best of 5: 54.7 msec per loop

5 function calls in 0.289 seconds
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
1    0.000    0.000    0.300    0.300 <string>:1(<module>)
1    0.000    0.000    0.300    0.300 p1_hw4.py:15(min_by_sort)
1    0.000    0.000    0.300    0.300 {built-in method builtins.exec}
1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
1    0.300    0.300    0.300    0.300 {method 'sort' of 'list' objects}
'''

def min_by_min(list_1, c=2):
    list_2, list_c = [], list_1.copy()
    for i in range(c):
        list_2.append(min(list_c))
        list_c.remove(list_2[i])
    return list_2


###size = 1000
# 100 loops, best of 5: 76.8 usec per loop
###size = 10000
# 100 loops, best of 5: 743 usec per loop
###size = 100000
# 100 loops, best of 5: 6.27 msec per loop
###size = 1000000
# 100 loops, best of 5: 97.8 msec per loop

# cProfile.run('min_by_min(rand_arr, 2)')
'''11 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.000    0.000    0.001    0.001 p1_hw4.py:50(min_by_min)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        2    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'copy' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        2    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}'''

def min_by_alg(a):
    if a[0] < a[1]:
        min1, min2 = 0, 1
    else:
        min1, min2 = 1, 0
    for i in range(2, len(a)):
        if a[i] < a[min1]:
            b = min1
            min1 = i
            if a[b] < a[min2]:
                min2 = b
        elif a[i] < a[min2]:
            min2 = i
    return a[min1], a[min2]

###size = 1000
# 100 loops, best of 5: 251 usec per loop
###size = 10000
# 100 loops, best of 5: 2.61 msec per loop
###size = 100000
# 100 loops, best of 5: 23.7 msec per loop

# cProfile.run('min_by_alg(rand_arr)')
'''5 function calls in 0.001 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.001    0.001 <string>:1(<module>)
        1    0.001    0.001    0.001    0.001 p1_hw4.py:82(min_by_alg)
        1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}'''
