expense_list = []
user= int(input("Enter how many days expense you want to do: "))
total_expense = 0
count = 0
count_1 = 0
for i in range(user):
    amount = int(input("enter your amount one byy one: "))
    expense_list.append(amount)
    total_expense += amount

    if amount >= 200 :
        print("High Expense")
        count += 1
    elif amount >= 100 :
        print("Medium Expense")
    elif amount >= 50 :
        print("Low Expense")
    elif amount < 50:
        print("Very LOW Expense")
        count_1 += 1
highest = max(expense_list)
highest_days = expense_list.index(highest)
lowest = expense_list[0]

for expense in expense_list:
    if expense < lowest:
        lowest = expense
lowest_days  = expense_list.index(lowest)

average = total_expense / len(expense_list)
print("Total Days is",user)
print("TOTAL EXPENSE IS",total_expense)
print("Average expense: ", average)
print("Highest expense: ", highest, highest_days + 1)
print("Lowest expense: ", lowest,lowest_days + 1)
print("High Expense days: ",count)
print("Lowest expense days: ",count_1)
