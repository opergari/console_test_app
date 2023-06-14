number = int(input("Введите трехзначное число: "))

digit1 = abs(number) // 100
digit2 = (abs(number) // 10) % 10
digit3 = abs(number) % 10

print(digit1)
print(digit2)
print(digit3)