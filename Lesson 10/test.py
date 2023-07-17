# with open('hw_10_test.txt', 'r', encoding='utf-8') as file:
#     text = {}
#     for line in file:
#         category = line.split()[-1]
#         money = float(line.split()[-2].strip('$'))
#         if category in text:
#             text[category] = text[category] + money
#         else:
#             text[category] = money
#
# print(text)

#result = {}
with open('hw_10_test.txt', 'r', encoding='utf-8') as file:
    for line in file:
        money = float(line.split()[-2].strip('$'))
        words = line.split()
        if len(words) == 4:
            user_name = words[1]
        else:
            user_name = words[1] + ' ' + words[2]


        print(user_name)


        # if user_name in result:
        #     result[user_name] = result[user_name] + money
        # else:
        #     result[user_name] = money





