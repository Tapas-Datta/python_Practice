

customer_name = input("Enter your name: ")
customer_available_balance = int(input("Enter your available balance: "))
product = int(input("Enter how many product you want to buy: "))
price_list = []
quantity_list = []
for i in range(product):
    product = input("Enter product name: ")
    Product_price = float(input("Enter product price: "))
    price_list.append(Product_price)
    product_quantity = int(input("Enter product quantity: "))
    quantity_list.append(product_quantity)
def calculate_order(price_list, quantity_list):
    subtotal_list = []
    total_order_amount = 0
    for i in range(len(price_list)):
        subtotal = price_list[i] * quantity_list[i]
        total_order_amount += subtotal
        subtotal_list.append(subtotal)
    return subtotal_list, total_order_amount

def calculate_discount(total_order_amount):
    if total_order_amount >= 500:
        discount = total_order_amount * 0.15
    elif total_order_amount >= 300:
        discount = total_order_amount * 0.10
    elif total_order_amount >= 100:
        discount = total_order_amount * 0.05
    else:
        discount = 0
    order_amount_after_discount = total_order_amount - discount
    return discount, order_amount_after_discount


def calculate_shipping(order_amount_after_discount):
    if order_amount_after_discount >= 200:
        shipping = 0
    else:
        shipping =15
    return shipping
def process_payment(order_amount_after_discount,customer_available_balance):
    if order_amount_after_discount > customer_available_balance:
        payment_status = "Payment Failed"
        remaining_amount = customer_available_balance
    else:
        payment_status = "payment successful"
        remaining_amount = customer_available_balance - order_amount_after_discount
    return payment_status, remaining_amount

def analyze_order(subtotal, product_list, quantity_list):
    most_expensive = subtotal[0]
    cheapest_product = subtotal[0]
    highest_quantity = quantity_list[0]
    highest_quantity_product = product_list[0]
    total_amount = 0
    total_quantity = 0

    for i in range(len(subtotal)):
        total_amount += subtotal[i]
        total_quantity += quantity_list[i]

        if subtotal[i] > most_expensive:
            most_expensive = subtotal[i]

        if subtotal[i] < cheapest_product:
            cheapest_product = subtotal[i]

        if quantity_list[i] > highest_quantity:
            highest_quantity = quantity_list[i]
            highest_quantity_product = product_list[i]

    return total_amount, total_quantity, most_expensive, cheapest_product, highest_quantity_product

subtotal_list, total_order_amount = calculate_order(price_list, quantity_list)

discount, order_amount_after_discount = calculate_discount(total_order_amount)

shipping = calculate_shipping(order_amount_after_discount)

final_payment_amount = order_amount_after_discount + shipping

payment_status, remaining_amount = process_payment(
    final_payment_amount, customer_available_balance
)

total_amount, total_quantity, most_expensive, cheapest_product, highest_quantity_product = analyze_order(
    subtotal_list, quantity_list
)

print("========== ORDER SUMMARY ==========")
print("Customer:", customer_name)
print("Total Quantity:", total_quantity)
print("Most Expensive Product Subtotal:", most_expensive)
print("Cheapest Product Subtotal:", cheapest_product)
print("Highest Quantity Product:", highest_quantity_product)
print("Subtotal:", total_order_amount)
print("Discount:", discount)

if shipping == 0:
    print("Shipping: FREE")
else:
    print("Shipping:", shipping)

print("Final Payment:", final_payment_amount)
print("Payment Status:", payment_status)
print("Remaining Balance:", remaining_amount)





    
        
