a = [1, 2, 6, 56, 78]
def number_int(num):
    for i in a:
        if i == num:
            return a.index(i)
    else:
        return -1
print(number_int(56))

