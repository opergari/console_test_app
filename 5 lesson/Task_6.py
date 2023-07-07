height = int(input("Введите высоту прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))

for i in range(height):
    for j in range(width):
        print("*", end=' ')
    print()

# n, m = int(input('n=')), int(input('m='))
# res = f"{'*' * n}\n" + f"*{' ' * (n - 2)}*\n" * (m - 2) + f"{'*' * n}\n"
# print(res)