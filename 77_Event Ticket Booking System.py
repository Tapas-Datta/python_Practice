sold_list = []
total_cost_list = []
name_list = []
count = 0
dis = 0
user = int(input("Enter how many bookings you have: "))
for i in range(user):
    name = input("Enter your name: ")
    name_list.append(name)
    ticket_type = input("Enter your ticket type Standard, VIP or Student: ")
    if ticket_type == "VIP":
        count += 1
    quantity = int(input("Enter the number of your tickets: "))
    sold_list.append(quantity)
    age = int(input("Enter your age: "))

    print("Customer name: ", name)
    print("Customer ticket type: ", ticket_type)
    print("total tickets: ",quantity)
    if ticket_type == "VIP":
        price  = 70
        total_cost = price * quantity
        print("average amount:",total_cost/quantity)
    elif ticket_type == "Standard":
        price = 30
        total_cost = price * quantity

        print("average amount:", total_cost / quantity)
    elif ticket_type == "Student":
        price = 15
        total_cost = price * quantity

        print("average amount:", total_cost / quantity)
    discount = 0
    if quantity >= 5:
        discount = total_cost * 0.10
    if age >= 60:
        age_discount = (total_cost - discount) * 0.05
    else:
        age_discount = 0
    if quantity >= 5 or age >= 60:
        dis += 1
    final_amount = total_cost - discount - age_discount
    total_cost_list.append(final_amount)
    print("Final Amount: ", final_amount)
highest = max(total_cost_list)
position = total_cost_list.index(highest)
name_1 = name_list[position]
lowest = min(total_cost_list)
position = total_cost_list.index(lowest)
name_2 = name_list[position]
print("total bookings:",user)
print("Total ticket sold: ", sum(sold_list))
print("total revenue: ", sum(total_cost_list))
print("Average amount per booking:", sum(total_cost_list) / len(total_cost_list))
print("Highest payment: ", highest , name_1)
print("Lowest payment: ", lowest , name_2)
print("vip ticket number: ",count)
print("Discount bookings:", dis)

