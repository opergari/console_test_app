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


# # Task 2
# vocabulary = {
#     'cat': 'кіт',
#     'dog': 'собака',
# }
#
# text = input('text=').lower().split()
# for item in text:
#     print(vocabulary.get(item, item), end=' ')

