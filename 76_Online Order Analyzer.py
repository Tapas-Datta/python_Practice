name_list = []
amount_list = []
item_list = []
count = 0
user = int(input("how many customer details you have?"))
for i in range(user):
    name = input("Enter customer name:")
    name_list.append(name)
    amount = int(input("Enter amount:"))
    amount_list.append(amount)
    items = int(input("Enter items:"))
    item_list.append(items)
    if amount >= 500:
        count += 1
        print("Large Order")
    elif 200 <= amount <  500:
        print( "Medium Order" )
    elif 0 < amount < 200:
        print("Small Order")
    else:
        print("negative or zero is not the product check again")
total_amount  =  sum(amount_list)
average_amount  = total_amount / len(amount_list)
highest = amount_list[0]
lowest = amount_list[0]
for amount in amount_list:
    if amount > highest:
        highest = amount
    if amount < lowest:
        lowest = amount

position = amount_list.index(highest)
name = name_list[position]
position = amount_list.index(lowest)
name_1 = name_list[position]
item_sold = sum(item_list)

print("Total Order is",user)
print("Total amount:",total_amount)
print("Average amount:",average_amount)
print("Highest amount:",highest,name)
print("Lowest amount:",lowest,name_1)
print("Total items sold:",item_sold)
print("Large orders:",count)

