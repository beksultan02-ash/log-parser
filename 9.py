names = ["Bob", "Alice", "Bob", "Tom", "Alice", "Sam"]
s_names = set(names)

names_unique = []

for i in names:
    if i in s_names:
        names_unique.append(i)
        s_names.remove(i)

print(names_unique)

