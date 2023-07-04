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