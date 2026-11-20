
user = int(input("How many products do you want to add to your shopping cart? "))
product = []
prices = []
quantityis = []

for i in range(user):
    name_of_product = input("What is the name of the product? ")
    product.append(name_of_product)
    price_1 = float(input("What is the price of the product? "))
    prices.append(price_1)
    quantity = int(input("What is the quantity of the product? "))
    quantityis.append(quantity)
def details(product, prices, quantityis):
    total_price = 0
    count = 0
    highest = prices[0]
    lowest = prices[0]
    expensive_product = product[0]
    cheapest_product = product[0]
    for i in range(len(prices)):
        total_price += prices[i] * quantityis[i]
        if prices[i] > 50:
            count += 1
        if prices[i] > highest:
            highest = prices[i]
            expensive_product = product[i]
        if prices[i] < lowest:
            lowest = prices[i]
            cheapest_product = product[i]
    average_price = 0
    for price in prices:
        average_price += price
    average_price = average_price / len(prices)
    return total_price, average_price, count, expensive_product, highest, cheapest_product, lowest


def final_bill(total_price):
    discount = total_price * 0.10
    final_price = total_price - discount
    return final_price, discount
total_price_3, average_price, count, expensive_product, highest, cheapest_product, lowest = details(product, prices, quantityis)
final_price, final_discount = final_bill(total_price_3)


print("\n========== SHOPPING CART ==========")
print("Total price:", total_price_3)
print("Average product price:", average_price)
print("Most expensive product:", expensive_product, "-", highest)
print("Cheapest product:", cheapest_product, "-", lowest)
print("Products above 50:", count)
print("Discount:", final_discount)
print("Final bill:", final_price)
