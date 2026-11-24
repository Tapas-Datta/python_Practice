
name_list = []
stock_list = []
sold_list = []
revenue_list = []
remaining_stock_list = []
user = int(input("how many products do you want to calculate? "))
total_sold = 0
total_stock = 0
total_revenue = 0
total_stock_value = 0
for i in range(user):

    product_name = input("Enter the product name: ")
    name_list.append(product_name)

    stock_quantity = int(input("Enter the initial quantity of the product: "))
    stock_list.append(stock_quantity)

    sold_quantity = int(input("Enter the quantity of the sold product: "))
    sold_list.append(sold_quantity)

    price_per_unit = int(input("Enter the price of the product: "))

    total_sold += sold_quantity
    total_stock += stock_quantity

    remaining_stock = stock_quantity - sold_quantity
    remaining_stock_list.append(remaining_stock)

    product_revenue = price_per_unit * sold_quantity
    total_revenue += product_revenue
    revenue_list.append(product_revenue)

    stock_value = remaining_stock * price_per_unit
    total_stock_value += stock_value

    print("--------------------------------")
    print("Product:", product_name)
    print("Total sold:", sold_quantity)
    print("Total stock:", stock_quantity)
    print("Remaining stock:", remaining_stock)
    print("Total revenue:", product_revenue)
    print("Stock value:", stock_value)
    print("--------------------------------")


def store_summary(stock_list, sold_list, revenue_list, remaining_stock_list, name_list):

    total_store_stock = 0
    total_store_sold = 0
    total_store_revenue = 0

    highest_revenue = revenue_list[0]
    lowest_revenue = revenue_list[0]

    highest_name = name_list[0]
    lowest_name = name_list[0]

    zero_stock_count = 0
    low_stock_count = 0

    for item in stock_list:
        total_store_stock += item

    for item_1 in sold_list:
        total_store_sold += item_1

    for revenue in revenue_list:
        total_store_revenue += revenue

    for i in range(len(revenue_list)):

        if revenue_list[i] > highest_revenue:
            highest_revenue = revenue_list[i]
            highest_name = name_list[i]

        if revenue_list[i] < lowest_revenue:
            lowest_revenue = revenue_list[i]
            lowest_name = name_list[i]

    for stock in remaining_stock_list:

        if stock == 0:
            zero_stock_count += 1

        if stock < 5:
            low_stock_count += 1

    total_store_remaining = 0

    for stock in remaining_stock_list:
        total_store_remaining += stock

    return (total_store_stock, total_store_sold, total_store_revenue,
            total_store_remaining, highest_name, lowest_name,
            highest_revenue, lowest_revenue, zero_stock_count,
            low_stock_count)


final = store_summary(stock_list, sold_list, revenue_list, remaining_stock_list, name_list)

(total_store_stock, total_store_sold, total_store_revenue,
 total_store_remaining, highest_name, lowest_name,
 highest_revenue, lowest_revenue, zero_stock_count,
 low_stock_count) = final


print("========================================")
print("Total products:", user)
print("Total stock:", total_store_stock)
print("Total sold:", total_store_sold)
print("Total remaining:", total_store_remaining)
print("Total revenue:", total_store_revenue)
print("Total stock value:", total_stock_value)
print("Highest revenue product:", highest_name, highest_revenue)
print("Lowest revenue product:", lowest_name, lowest_revenue)
print("Zero stock products:", zero_stock_count)
print("Products with stock below 5:", low_stock_count)
print("========================================")
