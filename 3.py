nums = [10, 50, 23, 44, 90, 12]

first_max = float('-inf')
second_max = float('-inf')

for i in nums:
    if i > first_max:
        second_max = first_max
        first_max = i
    elif i > second_max and i != first_max:
        second_max = i

print(first_max,second_max)