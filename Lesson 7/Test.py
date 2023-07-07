import operator
calc = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}
a, b = int(input('a= ')), int(input('b= '))
op = input('operation is ')
if op in calc:
    res = calc[op](a, b)
    print(f'Result is {res}')
else:
    print('Errore')

# def sub(a, b):
#     return a - b
#
#
# def add(a, b):
#     return a + b
#
#
# def calc(a, b, operator):
#     if operator == '+':
#         return add(a, b)
#     if operator == '-':
#         return sub(a, b)
#     return None
#
#
# x, y = int(input('a=')), int(input('b='))
# print(calc(x, y, '+'))
# print(calc(x, y, '-'))
# print(calc(x, y, '*'))