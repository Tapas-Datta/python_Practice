final_price_list = []
name_list = []
dis_count = 0
user  = int(input("Enter how many booking details you want to add "))
ticket_sold = 0
for i in range(user):
    customer_name = input("Enter customer name : ")
    ticket_type = input("Enter ticket type Regular, Premium, Student : ")
    ticket_quantity = int(input("Enter ticket quantity : "))
    if ticket_type not in ["Regular", "Premium", "Student"]:
        print("Invalid ticket type")
        continue
    name_list.append(customer_name)
    ticket_sold += ticket_quantity
    if ticket_type== "Regular":
        price = 12
    elif ticket_type == "Premium":
        price = 20
    elif ticket_type== "Student":
        price = 8
    if ticket_quantity >= 5:
        discount = 0.10
        dis_count +=1
    else:
        discount = 0
    total_price =(price * ticket_quantity)
    after_discount = discount *  total_price
    final_price = total_price - after_discount
    final_price_list.append(final_price)
total_revenue = sum(final_price_list)
average_booking_cost = total_revenue / len(final_price_list)

highest_payment = max(final_price_list)
position = final_price_list.index(highest_payment)
cus_name = name_list[position]

lowest_payment = min(final_price_list)
position_1 = final_price_list.index(lowest_payment)
cus_name_1 = name_list[position_1]

print("Total tickets sold",ticket_sold)
print("Total revenue: ", total_revenue)
print("Average booking cost: ", average_booking_cost)
print("Highest payment: ", highest_payment,cus_name)
print("Lowest payment: ", lowest_payment,cus_name_1)
print("Number of bookings with discount:", dis_count)



    