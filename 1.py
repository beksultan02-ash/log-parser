def func(x):
    result = []
    while x > 0:
        result.append(x)
        x = x - 1
    return result

n = int(input("Введите число"))
print(*func(n))
