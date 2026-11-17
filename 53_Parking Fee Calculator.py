costs = 0
count = 0
total_collected = 0
highest_fee = 0
while True:
    user = float(input("Enter the number of hours you want to parked: "))
    if user == 0:
        break
    count += 1
    if user > int(user):
        user = int(user) + 1
    if 0< user <= 1:
        costs = 2
        total_collected += costs
        print("Parking duration is: ",user)
        print("Costs is:", costs)

    elif user <= 5:
        costs= ((1 * 2 ) +(user -1) * 1.50)
        total_collected += costs
        print("Parking duration is: ", user)
        print("Costs is:", costs)

    elif user > 5:
        costs = ((1 * 2 ) +(4 * 1.50) + ((user -5) * 1 ))
        total_collected += costs
        print("Parking duration is: ", user)
        print("Costs is:", costs)
    if costs > 12:
        costs = 12
    if costs > highest_fee:
        highest_fee = costs

print("Vehicle passed is", count)
print("Total collected is:", total_collected)
print("Highest fee is:", highest_fee)
















