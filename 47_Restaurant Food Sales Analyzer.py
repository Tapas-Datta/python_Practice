name_1 =input("Enter the name of your restaurant: ")
sold_item = int(input("Enter the number of sold items: "))
all_item_price_list = []
for i in range(sold_item):
    name = input ("Enter the food name: ")
    price = float(input ("Enter the price of the item: "))
    quantity = int(input ("Enter the quantity of the item: "))
    total_price = price * quantity
    all_item_price_list.append(total_price)

def analyze_sales(all_item_price_list):
    if not all_item_price_list:
        return None
    count =0
    count_1 = 0
    highest_sale = all_item_price_list[0]
    lowest_sale = all_item_price_list[0]
    total_revenue = 0
    for item in all_item_price_list:
        total_revenue += item
        if item > highest_sale:
            highest_sale = item
        if item < lowest_sale:
            lowest_sale = item
        if item >= 50:
            count +=1
        if item < 20:
            count_1 += 1
    if total_revenue >= 200:
        discount = total_revenue * 0.10
        final_sale = total_revenue - discount
    else:
        discount = 0
        final_sale = total_revenue - discount
    average_revenue = total_revenue / len(all_item_price_list)
    return total_revenue,average_revenue, highest_sale, lowest_sale ,count, count_1, discount, final_sale
result = analyze_sales(all_item_price_list)
if result is None:
    print("No data entered.")
else:
    total_revenue, average_revenue, highest_sale, lowest_sale, count, count_1, discount, final_sale= result
    print"----------------------------------"
    print("Restaurant Name:", name_1)
    print("Total revenue: ",total_revenue)
    print("Average sales: ",average_revenue)
    print("Highest sale: ",highest_sale)
    print("Lowest sale: ",lowest_sale)
    print("Count with more than 50: ",count)
    print("Count below 20: ",count_1)
    print(f"discount: {discount:.2f}")
    print("Final sale: ",final_sale)


