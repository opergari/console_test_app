leap_year = int(input('Введите год: '))
leap_year = 'Высокосный год!' if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0 else 'Это не высокосный год!'
print(leap_year)