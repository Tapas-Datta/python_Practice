values = [2, 7, 4, 9, 3, 5]
count = 0
index = []
for i in range(1, len(values) - 1):
    if values[i] > values[i - 1] and values[i] > values[i + 1]:
        index.append(i)
        count += 1
print(index)

