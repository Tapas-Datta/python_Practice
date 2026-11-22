number_list = []
for i in range(1, 11):
    number = int(input("please, enter your number serially: "))
    number_list.append(number)
def consecutive_run(number_list):
    current_sequence = [number_list[0]]
    longest_sequence = [number_list[0]]
    current_start = 0
    longest_start = 0

    for i in range(1, len(number_list)):
        if number_list[i] > number_list[i - 1]:
            current_sequence.append(number_list[i])
        else:
            current_sequence = [number_list[i]]
            current_start = i

        if len(current_sequence) > len(longest_sequence):
            longest_sequence = current_sequence[:]
            longest_start = current_start

    return longest_sequence, longest_start

final_sequence, start_index = consecutive_run(number_list)

print("Longest increasing sequence:", final_sequence)
print("Length:", len(final_sequence))
print("Starting index:", start_index)

    
