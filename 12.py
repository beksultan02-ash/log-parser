text = "apple banana apple orange banana apple"
words = text.split()
count = {}

for i in words:
    count[i] = count.get(i, 0) + 1

print(count)