# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов.
# Результаты анализа сохранить в виде комментариев в файле с кодом.

# import cProfile
import timeit

def erat_sieve(y):
    n = 1000
    a = [i for i in range(n)]
    a[1], m = 0, 2
    while m < n:
        if a[m] != 0:
            j = m * 2
            while j < n:
                a[j] = 0
                j = j + m
        m += 1
    a = [i for i in a if a[i] != 0]
    return a[y - 1]

# _hw4.erat_sieve(10)"
# 100 loops, best of 5: 420 usec per loop
# _hw4.erat_sieve(20)"
# 100 loops, best of 5: 417 usec per loop
# _hw4.erat_sieve(50)"
# 100 loops, best of 5: 420 usec per loop


# cProfile.run('erat_sieve(20)')
''' 6 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 p2_hw4.py:10(erat_sieve)
        1    0.000    0.000    0.000    0.000 p2_hw4.py:12(<listcomp>)
        1    0.000    0.000    0.000    0.000 p2_hw4.py:21(<listcomp>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''



def f_p_num_by_div(y):
    num, pos_n = 2, 0 #int(input('Введите номер простого числа: '))
    while True:
        if num != 4:
            for i in range(2, int(num * 0.5)):
                if num % i == 0:
                    break
            else:
                pos_n += 1
                if pos_n == y:
                    return num
        num += 1

# _hw4.f_p_num_by_div(5)"
# 100 loops, best of 5: 5.47 usec per loop

# _hw4.f_p_num_by_div(100)"
# 100 loops, best of 5: 964 usec per loop

# _hw4.f_p_num_by_div(1000)"
# 100 loops, best of 5: 144 msec per loop

# cProfile.run('f_p_num_by_div(15)')

'''         4 function calls in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 p2_hw4.py:41(f_p_num_by_div)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''
