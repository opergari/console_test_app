def word_count(text):
    return len(text.split())
print(word_count('dgfsdgd dfdsf gsdf dsag 6 8980  '))


# Task 4
# def words_count(text: str, punctuations=' ,:.!?-'):
#     for item in punctuations:
#         text = text.replace(item, ' ')
#     return len(text.split())
#
#
# text = input('text=')
# print(words_count(text))