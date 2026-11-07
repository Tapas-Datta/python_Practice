first_item = input("Enter the first item: ")
first_item_price = float(input("Enter the first item price: "))
second_item = input("Enter the second item: ")
second_item_price = float(input("Enter the second item price: "))
third_item = input("Enter the third item: ")
third_item_price = float(input("Enter the third item price: "))
fourth_item = input("Enter the fourth item: ")
fourth_item_price = float(input("Enter the fourth item price: "))
fifth_item = input("Enter the fifth item: ")
fifth_item_price = float(input("Enter the fifth item price: "))

all_items = [first_item, second_item, third_item, fourth_item, fifth_item]
all_item_prices = [first_item_price, second_item_price, third_item_price, fourth_item_price, fifth_item_price]

if any(price <= 0 for price in all_item_prices):
    print("Invalid price")
else:
    print("Shopping Cart:", all_items)
    print("Item Prices:", all_item_prices)

    total_item_price = 0
    for price in all_item_prices:
        total_item_price += price

    print("Total Price:", total_item_price)

    average_price = total_item_price / len(all_items)
    print("Average Price:", average_price)

    if total_item_price > 1000:
        discount = total_item_price * 0.10
    else:
        discount = total_item_price * 0

    print("Discount:", discount)

    final_bill = total_item_price - discount
    print("Final Bill:", final_bill)