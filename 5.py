matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

row = len(matrix)
colums = len(matrix[0])
trans = []

for j in range(colums):
    new_row = []
    for i in range(row):

        new_row.append(matrix[i][j])
    trans.append(new_row)

print("Common matrix:")

for rows in matrix:
    print(*rows)

print("Transported:")

for tr in trans:
    print(*tr)

print()
