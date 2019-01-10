# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны любому из чисел в диапазоне от 2 до 9.

nat_int = {i: i for i in range(2, 100)}
for i in nat_int.keys():
    k = 0
    for j in range(2, 10):
        if i % j == 0:
            k += 1
    nat_int[i] = k

print(nat_int)
