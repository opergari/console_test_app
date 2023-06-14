numbers = []
for i in range(5):
    number = int(input("Введите целое число: "))
    numbers.append(number)

# Нахождение минимума, максимума и среднего значения
minimum = min(numbers)
maximum = max(numbers)
average = (max(numbers) + min(numbers)) / 2

# Вывод результатов
print("Минимум:", minimum)
print("Максимум:", maximum)
print("Среднее:", average)