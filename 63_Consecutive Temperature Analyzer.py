
temperatures = []

for user in range(1, 11):
    temperature_1 = int(input("Enter the temperature: "))
    temperatures.append(temperature_1)
def temp(temperatures):
    highest = temperatures[0]
    lowest = temperatures[0]
    total_temperatures = 0
    negative_temperatures = 0
    for temperature in temperatures:
        total_temperatures += temperature
        if temperature > highest:
            highest = temperature
        if temperature < lowest:
            lowest = temperature
        if temperature < 0:
            negative_temperatures += 1
    average = total_temperatures / len(temperatures)
    count = 0
    for i in range(len(temperatures)):
        if temperatures[i] > average:
            count += 1
    return average, highest, lowest, count, negative_temperatures
def consecutive_run(temperatures):
    run_list = [temperatures[0]]
    count_1 = 1
    highest_run = 1
    longest_sequence = [temperatures[0]]
    for j in range(len(temperatures) - 1):
        if temperatures[j] < temperatures[j + 1]:
            run_list.append(temperatures[j + 1])
            count_1 += 1
        else:
            run_list = [temperatures[j + 1]]
            count_1 = 1
        if count_1 > highest_run:
            highest_run = count_1
            longest_sequence = run_list.copy()

    return longest_sequence, highest_run


average, highest, lowest, count, negative = temp(temperatures)
longest_sequence, highest_run = consecutive_run(temperatures)

print("\n========== TEMPERATURE ANALYSIS ==========")

print("Average temperature:", average)
print("Highest temperature:", highest)
print("Lowest temperature:", lowest)
print("Above average days:", count)
print("Negative temperature days:", negative)

print("Longest increasing sequence:", longest_sequence)
print("Sequence length:", highest_run)
