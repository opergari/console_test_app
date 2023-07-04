summa = 0
count = 0
num = 1

while num <= 99:
    if num % 2 != 0:
        summa += num
        count += 1
    num += 1
print(summa)
