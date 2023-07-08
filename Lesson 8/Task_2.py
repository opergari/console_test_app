def square_data(a, b):
    return f"{'*' * a}\n" + f"*{' ' * (a - 2)}*\n" * (b - 2) + f"{'*' * a}\n"
print(square_data(4, 5))
