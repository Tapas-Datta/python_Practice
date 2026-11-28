name_list = []
quantity_list = []
unit_price_list = []

user = int(input("Enter how many products you want to add: "))

for i in range(user):
    name = input("Enter product name: ")
    quantity = int(input("Enter quantity: "))
    unit_price = float(input("Enter product unit price: "))

    if name in name_list:
        position = name_list.index(name)
        quantity_list[position] += quantity
    else:
        name_list.append(name)
        quantity_list.append(quantity)
        unit_price_list.append(unit_price)

total_quantity = sum(quantity_list)
total_value = 0
total_price_list = []

for i in range(len(name_list)):
    total_price = quantity_list[i] * unit_price_list[i]
    total_price_list.append(total_price)
    total_value += total_price

highest_price = max(total_price_list)
highest_position = total_price_list.index(highest_price)
high_product = name_list[highest_position]

lowest_price = min(total_price_list)
lowest_position = total_price_list.index(lowest_price)
low_product = name_list[lowest_position]

low_quantity_products = []

for i in range(len(name_list)):
    if quantity_list[i] < 5:
        low_quantity_products.append(name_list[i])

print("Total quantity:", total_quantity)
print("Total inventory value:", total_value)
print("Highest value product:", high_product, highest_price)
print("Lowest value product:", low_product, lowest_price)
print("Products with quantity under 5:", low_quantity_products)