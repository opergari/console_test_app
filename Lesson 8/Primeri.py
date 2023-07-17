def sub(a, b):
    return a - b


def add(a, b):
    return a + b


def calc(a, b, operator):
    if operator == '+':
        return add(a, b)
    if operator == '-':
        return sub(a, b)
    return None


x, y = int(input('a=')), int(input('b='))
print(calc(x, y, '+'))
print(calc(x, y, '-'))
print(calc(x, y, '*'))