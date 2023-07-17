from num2words import num2words
def my_currency_account(num):
    return f'{num2words(int(num))} dollars  {num2words(round((num % 1) * 100))} cents'
print(my_currency_account(9874.25))


# Task 5
# import num2words
# print(num2words.num2words(123.34, lang='uk'))
