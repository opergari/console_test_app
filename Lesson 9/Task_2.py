
# def palindrom(start, stop):
#     if start > stop:
#         stop, start = start, stop
#     res = []
#     for i in range(start, stop):
#         for j in range(start, stop):
#             tmp = str(i * j)
#             if tmp == tmp[::-1]:
#                 res.append((i * j, i, j))
#
#     return max(res, key=lambda item: item[0])
#
#
# print(*palindrom(10, 100))

