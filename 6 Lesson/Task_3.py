a = input('a= ')
n = []
for i in a:
    if i.isdigit():
        n.append(int(i))
print(sum(n))