side_a = int(input('Введите сторону A: '))
side_b = int(input('Введите сторону B: '))
side_c = int(input('Введите сторону C: '))
if side_a + side_b >= side_c and side_a + side_c >= side_b and side_b + side_c >= side_a:
    print('Триугольник с такими сторонами валиден!')

else:
    print('Триугольник с такими сторонами невалиден!')