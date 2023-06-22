points = int(input('Введите ваши очки: '))
if 90 <= points <= 100:
    print('A')
elif 85 <= points <= 89:
    print('B')
elif 75 <= points <= 84:
    print('C')
elif 70 <= points <= 74:
    print('D')
elif 60 <= points <= 69:
    print('E')
elif 0 <= points <= 60:
    print('E')
else:
    print('Errore')