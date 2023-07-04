a = input('test= ')
a = a.split()
res = {}
for words in a:
    if words not in res:
        res[words] = a.count(words)
print(res)

