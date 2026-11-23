unit_list = []
name_list = []
user = int(input("Enter how many customer bills you want to input: "))
for i in range(user):
    customer_name = input("Enter customer name: ")
    name_list.append(customer_name)

    electricity_units_consumed = int(input("Enter electricity units consumed: "))
    unit_list.append(electricity_units_consumed)
    
def bills_count(unit):

    if unit <= 100:
        bills = unit * 0.10

    elif unit <= 200:
        bills = (100 * 0.10) + (unit - 100) * 0.15

    else:
        bills = (100 * 0.10) + (100 * 0.15) + (unit - 200) * 0.20
    return bills
total_revenue = 0
highest_bill = 0
lowest_bill = 0
total_bills = []
for j in range(user):
    bills = bills_count(unit_list[j])
    tax = bills * 0.10
    final_bill = bills + tax
    total_bills.append(final_bill)
    total_revenue += final_bill
    if j == 0:
        highest_bill = final_bill
        lowest_bill = final_bill
    if final_bill > highest_bill:
        highest_bill = final_bill
    if final_bill < lowest_bill:
        lowest_bill = final_bill
    print("\n==============================")
    print("Customer name:", name_list[j])
    print("Units consumed:", unit_list[j])
    print("Electricity bill:", bills)
    print("Tax:", tax)
    print("Final bill:", final_bill)

average_bill = total_revenue / user
print("\n========== COMPANY SUMMARY ==========")
print("Total revenue:", total_revenue)
print("Average bill:", average_bill)
print("Highest bill:", highest_bill)
print("Lowest bill:", lowest_bill)
