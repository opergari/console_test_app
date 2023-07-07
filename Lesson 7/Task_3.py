contacts = {}

while True:
    print("\nМеню:")
    print("1. Добавить контакт")
    print("2. Удалить контакт")
    print("3. Получить номер телефона")
    print("4. Выйти")

    choice = input("Введите номер операции: ")

    if choice == "1":
        name = input("Введите имя контакта: ")
        phone_number = input("Введите номер телефона: ")
        contacts[name] = phone_number
        print("Контакт успешно добавлен!")

    elif choice == "2":
        name = input("Введите имя контакта для удаления: ")
        if name in contacts:
            del contacts[name]
            print("Контакт успешно удален!")
        else:
            print("Контакт не найден.")

    elif choice == "3":
        name = input("Введите имя контакта для получения номера телефона: ")
        if name in contacts:
            phone_number = contacts[name]
            print(f"Номер телефона для контакта '{name}': {phone_number}")
        else:
            print("Контакт не найден.")

    elif choice == "4":
        print("Программа завершена.")
        break

    else:
        print("Неверный ввод. Пожалуйста, выберите операцию из списка.")

# # Task 3
# contacts = {}
# menu = 'Add new item - add\nUpdate item - update\nDelete item - del\nDet item - get\nGet contacts-all\nExit - exit\n'
#
# while (answer := input(menu).lower()) != 'exit':
#     if answer == 'add':
#         name, phone = input('name='), input('phone')
#         contacts[name] = phone
#     elif answer == 'update':
#         name, phone = input('name='), input('phone')
#         if name not in contacts:
#             print('Input error!')
#             continue
#         contacts[name] = phone
#     elif answer == 'del':
#         name = input('name=')
#         if name not in contacts:
#             print('Input error!')
#             continue
#         del contacts[name]
#     elif answer == 'get':
#         name = input('name=')
#         print(contacts.get(name, 'Input error!'))
#     elif answer == 'all':
#         for key, value in contacts.items():
#             print(f'{key} - {value}')