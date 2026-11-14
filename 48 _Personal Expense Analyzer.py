
name = input("Enter your name: ")
record= int(input("Enter how many record you want to have : "))


amount = []
for i in range(record):
    expense_name = input("Enter your expense name: ")
    expense_amount = int(input("Enter your expense amount: "))

    amount.append(expense_amount)
def analyze_expenses(amount):
    if not amount:
        return None
    total_expenses = 0
    highest_expense = amount[0]
    lowest_expense = amount[0]
    count = 0
    count_1 = 0
    for item in amount:
        total_expenses += item
        if item > highest_expense:
            highest_expense =item
        if item < lowest_expense:
            lowest_expense = item
        if item >= 50:
            count += 1
        if item < 20:
            count_1 += 1
    if total_expenses > 200:
        savings = total_expenses * 0.10
    else:
        savings = 0
    remaining_expenses = total_expenses - savings
    average = total_expenses / len(amount)
    return total_expenses, average, highest_expense, lowest_expense, count, count_1, savings, remaining_expenses
result = analyze_expenses(amount)
if result is None:
    print("No data entered.")
else:
    total_expenses,average,highest_expense, lowest_expense, count, count_1, savings, remaining_expenses = result
    print("--------____________----------")
    print("Name",name)
    print("Total expenses",total_expenses)
    print("Average expenses",average)
    print("Highest expense",highest_expense)
    print("Lowest expense",lowest_expense)
    print("Expense >= €50",count)
    print("Expense <= €20",count_1)
    print("Savings",savings)
    print("Remaining expenses",remaining_expenses)
    





    
