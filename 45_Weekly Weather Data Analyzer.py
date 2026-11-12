
temperature = []
name = input("Enter your name: ")
days = int(input("Enter how many days you want to calculate: "))
for i in range(days):
    temp = int(input("Enter temperature: "))
    temperature.append(temp)

def analyze_weather(temperatures):
    highest_temp = temperatures[0]
    lowest_temp = temperatures[0]
    total = 0
    hot_days = 0
    cold_days = 0
    for temp_1 in temperatures:
        total += temp_1

        if temp_1 > highest_temp:
            highest_temp = temp_1
        if temp_1 < lowest_temp:
            lowest_temp = temp_1

        if temp_1 >= 30:
            hot_days += 1

        if temp_1 < 15:
            cold_days += 1

    average = total / len(temperatures)
    if average < 10:
        condition = "Very Cold"
    elif average < 20:
        condition = "Cold"
    elif average < 30:
        condition = "Moderate"
    else:
        condition = "Hot"

    return average, highest_temp, lowest_temp, hot_days, cold_days, condition

result = analyze_weather(temperature)

average, highest, lowest, hot_days, cold_days, condition = result
print("----------------------------------------------------")
print("Customer:", name)
print("Average Temperature:", round(average, 2))
print("Highest Temperature:", highest)
print("Lowest Temperature:", lowest)
print("Hot Days:", hot_days)
print("Cold Days:", cold_days)
print("Condition:", condition)
