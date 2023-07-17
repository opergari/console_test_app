def is_arithmetic(sequence):
    if len(sequence) < 2:
        return False
    d = sequence[1] - sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i + 1] - sequence[i] != d:
            return False
    return True


def next_arithmetic(sequence):
    d = sequence[1] - sequence[0]
    return sequence[-1] + d


def is_geometric(sequence):
    if len(sequence) < 2:
        return False
    q = sequence[1] // sequence[0]
    for i in range(len(sequence) - 1):
        if sequence[i + 1] // sequence[i] != q:
            return False
    return True


def next_geometric(sequence):
    q = sequence[1] // sequence[0]
    return sequence[-1] * q


def sequence_process(sequence):
    if is_arithmetic(sequence):
        return next_arithmetic(sequence)

    if is_geometric(sequence):
        return next_geometric(sequence)

    return None


sequence = input().strip().replace(',', ' ').split()
sequence = list(map(int, sequence))
res = sequence_process(sequence)
print(f'Next item is {res}')