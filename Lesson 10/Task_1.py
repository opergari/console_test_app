def total_expenses_by_categories(file_name: str):
    result = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            category = line.split()[-1]
            money = float(line.split()[-2].strip('$'))
            if category in result:
                result[category] += money
            else:
                result[category] = money
    return result


def total_expenses_by_users(file_name: str):
    result = {}
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            money = float(line.split()[-2].strip('$'))
            words = line.split()
            if len(words) == 4:
                user_name = words[1]
            else:
                user_name = words[1] + ' ' + words[2]
            if user_name in result:
                result[user_name] += money
            else:
                result[user_name] = money


    return result


def total_expenses_by_user_name(file_name: str, username: str):
    result_1 = 0
    result_2 = 0
    with open(file_name, 'r', encoding='utf-8') as file:
        for line in file:
            money = float(line.split()[-2].strip('$'))
            words = line.split()
            if len(words) == 4:
                current_user_name = words[1]
            else:
                current_user_name = words[1] + ' ' + words[2]
            if username == current_user_name:
                result_1 += 1
                result_2 += money

    return result_1, result_2


print(total_expenses_by_categories('hw_10_test.txt'))
print(total_expenses_by_users('hw_10_test.txt'))
print(total_expenses_by_user_name('hw_10_test.txt', input('username is ').strip()))