data = (10, 20, 30, 40, 50)
a = 0
b = []
c = []

for i in range(len(data)):
    if i == 0:
        a = data[i]
    elif i >= len(data) - 2:
        b.append(data[i])
    else:
        c.append(data[i])

print(a,b,c, end=" ")