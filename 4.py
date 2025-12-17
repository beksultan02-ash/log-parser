nums = [1, 3, 5, 3, 1, 7, 5]
result = []

for i in nums:
    duplicate = False
    for j in result:
        if i == j:
            duplicate = True
            break
    if not duplicate:
        result.append(i)

print(result)
    