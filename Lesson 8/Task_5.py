from num2words import num2words
def my_currency_account(num):
    print(f'{num2words(int(num))} dollars  {num2words(round((num % 1) * 100))} cents')
my_currency_account(9874.25)
