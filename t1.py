# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

i = str(input('Введите трёхзначное число: '))
print(f' Сумма цифр: {int(i[0]) + int(i[1]) + int(i[2])}, произведение цифр: {int(i[0]) * int(i[1]) * int(i[2])}')
