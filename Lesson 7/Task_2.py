text = input('Введите слово на английском:(hello,goodbye, cat, dog, house)  ')
translations = {
    'hello': 'привет',
    'goodbye': 'до свидания',
    'cat': 'кошка',
    'dog': 'собака',
    'house': 'дом'
}
for item in translations:
    if text in item:
        print(f'{item} - {translations[item]}')




