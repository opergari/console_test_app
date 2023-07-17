a = [1, 2, 6, 56, 78]
def number_int(num):
    for i in a:
        if i == num:
            return a.index(i)
    else:
        return -1
print(number_int(56))

# Task 3
def left_liner_search(sequence, x):
    for index, item in enumerate(sequence):
        if item == x:
            return index
    return -1


# def right_liner_search(sequence, x):
#     for index in range(len(sequence) - 1, -1, -1):
#         if sequence[index] == x:
#             return index
#     return -1
#
#
# def all_liner_search(sequence, x):
#     result = []
#     for index, item in enumerate(sequence):
#         if item == x:
#             result.append(index)
#     return result
#
#
# import random
# s = [random.randint(1, 10) for _ in range(10)]
# print(s)
# print(left_liner_search(s, 5))
# print(right_liner_search(s, 5))
# print(all_liner_search(s, 5))