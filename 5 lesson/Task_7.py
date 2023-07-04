x = [0, 5, 2, 4, 7, 1, 3, 19]
sum_odd = 0

for i in x:
    if i % 2 != 0:
        sum_odd += i

print("Сумма нечетных чисел:", sum_odd)