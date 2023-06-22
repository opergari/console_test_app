apartments_per_floor = 4
floors_per_entrance = 9
apartments_per_entrance = apartments_per_floor * floors_per_entrance
entrances = 4

apartment_number = int(input("Введите номер квартиры: "))

entrance_number = (apartment_number - 1) // apartments_per_entrance + 1
floor_number = ((apartment_number - 1) % apartments_per_entrance) // apartments_per_floor + 1
apartment_per_floor_number = (apartment_number - 1) % apartments_per_floor + 1
if apartment_number > apartments_per_floor * floors_per_entrance * entrances:
    print('Квартиры с таким номером не в этом доме!')
else:
    print(f'Ваша квартира находится в подьезде {entrance_number} на {floor_number} етаже {apartment_per_floor_number} по счету слево!')