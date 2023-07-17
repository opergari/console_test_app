def square_data(a, b):
    return f"{'*' * a}\n" + f"*{' ' * (a - 2)}*\n" * (b - 2) + f"{'*' * a}\n"
print(square_data(4, 5))


# Task 2
# def rectangle(width: int, height: int):
#     return f"{'*' * width}\n" * height
#
#
# a, b = int(input('a=')), int(input('b='))
# print(rectangle(a, b))