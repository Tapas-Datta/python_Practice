numbers = []
count = 0

while count < 10:
    user = int(input("Enter a number: "))
    numbers.append(user)
    count += 1

longest_sequence = [numbers[0]]
current_sequence = [numbers[0]]
starting_index = 0
current_index = 0

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        current_sequence.append(numbers[i])

    else:
        current_sequence = [numbers[i]]
        current_index = i

    if len(current_sequence) > len(longest_sequence):
        longest_sequence = current_sequence.copy()
        starting_index = current_index

print("Longest increasing sequence:", longest_sequence)
print("Starting index:", starting_index)
print("Length:", len(longest_sequence))