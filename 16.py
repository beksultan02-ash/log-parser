a = {"apple": 2, "orange": 3}
b = {"apple": 4, "banana": 10}
c = {}

for keys, value in a.items():
    c[keys] = value

for keys, value in b.items():
    if keys in c:
        c[keys] += value
    else:
        c[keys] = value

print(c)
