manager = int(input("Enter how many delivery drivers: "))
names_list = []
numbers_list = []
for i in range(manager):
    days_list = []
    driver = input("Enter driver name: ")
    names_list.append(driver)
    for j in range(1, 8):
        days = int(input("Enter amount of deliveries: "))
        days_list.append(days)
    numbers_list.append(days_list)
def individual_driver_analysis(numbers_list):
    total_deliveries = 0
    highest = numbers_list[0]
    lowest = numbers_list[0]
    zero_delivery_days = 0
    highest_days = []
    lowest_days = []

    for i in range(len(numbers_list)):
        number = numbers_list[i]
        total_deliveries += number
        if number > highest:
            highest = number
        if number < lowest:
            lowest = number
        if number == 0:
            zero_delivery_days += 1
    average_deliveries = total_deliveries / 7
    for i in range(len(numbers_list)):
        if numbers_list[i] == highest:
            highest_days.append(i + 1)
        if numbers_list[i] == lowest:
            lowest_days.append(i + 1)
    highest_run = 1
    count = 1
    longest_sequence = [numbers_list[0]]
    current_sequence = [numbers_list[0]]
    for i in range(1, len(numbers_list)):
        if numbers_list[i] > numbers_list[i - 1]:
            count += 1
            current_sequence.append(numbers_list[i])
        else:
            count = 1
            current_sequence = [numbers_list[i]]
        if count > highest_run:
            highest_run = count
            longest_sequence = current_sequence.copy()

    return total_deliveries, average_deliveries, highest, lowest, zero_delivery_days, highest_days, lowest_days, highest_run, longest_sequence
total_company = 0
company_average = 0
company_days = [0, 0, 0, 0, 0, 0, 0]

best_driver = []
lowest_driver = []
above_average_drivers = []
days_all_drivers = []

highest_streak = 0
streak_drivers = []

total_list = []

for i in range(manager):
    result = individual_driver_analysis(numbers_list[i])

    total_deliveries = result[0]
    average_deliveries = result[1]
    highest = result[2]
    lowest = result[3]
    zero_delivery_days = result[4]
    highest_days = result[5]
    lowest_days = result[6]
    highest_run = result[7]
    longest_sequence = result[8]

    total_list.append(total_deliveries)
    total_company += total_deliveries

    print("\nDriver:", names_list[i])
    print("Total deliveries:", total_deliveries)
    print("Average deliveries:", average_deliveries)
    print("Highest deliveries:", highest)
    print("Lowest deliveries:", lowest)
    print("Zero delivery days:", zero_delivery_days)
    print("Highest delivery days:", highest_days)
    print("Lowest delivery days:", lowest_days)
    print("Longest increasing streak:", longest_sequence)
    print("Longest streak length:", highest_run)

    if highest_run > highest_streak:
        highest_streak = highest_run
        streak_drivers = [names_list[i]]

    elif highest_run == highest_streak:
        streak_drivers.append(names_list[i])

    for j in range(7):
        company_days[j] += numbers_list[i][j]


company_average = total_company / manager

highest_company = total_list[0]
lowest_company = total_list[0]

for i in range(manager):
    if total_list[i] > highest_company:
        highest_company = total_list[i]

    if total_list[i] < lowest_company:
        lowest_company = total_list[i]

    if total_list[i] > company_average:
        above_average_drivers.append(names_list[i])

    if total_list[i] == highest_company:
        best_driver = [names_list[i]]

    elif total_list[i] > highest_company:
        best_driver = [names_list[i]]

    if total_list[i] == lowest_company:
        lowest_driver = [names_list[i]]

    elif total_list[i] < lowest_company:
        lowest_driver = [names_list[i]]


highest_company_day = company_days[0]

for i in range(7):
    if company_days[i] > highest_company_day:
        highest_company_day = company_days[i]

highest_days = []

for i in range(7):
    if company_days[i] == highest_company_day:
        highest_days.append(i + 1)

    all_present = True

    for j in range(manager):
        if numbers_list[j][i] < 10:
            all_present = False
    if all_present:
        days_all_drivers.append(i + 1)

print("\n========== COMPANY ANALYSIS ==========")
print("Total company deliveries:", total_company)
print("Average deliveries per driver:", company_average)
print("Best performing driver:", best_driver)
print("Lowest performing driver:", lowest_driver)
print("Company highest delivery:", highest_company_day)
print("Highest delivery days:", highest_days)
print("Drivers above company average:", above_average_drivers)
print("Days when all drivers delivered at least 10:", days_all_drivers)
print("Longest increasing streak length:", highest_streak)
print("Drivers with longest increasing streak:", streak_drivers)


user = int(input("Enter a number: "))
factorial = 1
for i  in range(user ,1 ,-1):
    factorial *= i
print(factorial)


user = int(input("Enter a number: "))
factorial = 1
factorial2 = []
for i in range(user ,0 ,-1):
    factorial *= i
    factorial2.append(i)
print(factorial)
print(factorial2)

