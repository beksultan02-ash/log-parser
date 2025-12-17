matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
sum_of_el = 0

for row in range(len((matrix))):
    for col in range(len(matrix[0])):
        if row == col:
            sum_of_el += matrix[row][col]

print(sum_of_el)
