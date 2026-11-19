values = []
threshold_1 = int(input("Enter the threshold: "))
measurements = int(input("Enter the number of measurements: "))
for measurement in range(measurements):
    user = int(input("Enter your values: "))
    values.append(user)
def indexes_above(values, threshold):
    positions = []
    for index, value in enumerate(values):
        if value > threshold:
            positions.append(index)
    return positions
def longest_consecutive_run(values, threshold):
    highest = 0
    count = 0
    total = 0
    highest_total = 0
    for value in values:
        if value > threshold:
            count += 1
            total += value
            if count > highest:
                highest = count
                highest_total = total
        else:
            count = 0
            total = 0
    return highest, highest_total
final = indexes_above(values, threshold_1)
final_1, final_2 = longest_consecutive_run(values, threshold_1)
print("Above threshold:", len(final))
print("Indexes:", final)
if final_1 == 0:
    print("Longest run length: 0")
    print("No run above threshold.")
else:
    print("Longest run length:", final_1)
    print("Longest run average:", f"{final_2 / final_1:.2f}")