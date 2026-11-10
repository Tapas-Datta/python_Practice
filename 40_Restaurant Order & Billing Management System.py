user = input("Enter your name: ")
print("Welcome to our restaurant", user)
print("Here is our menu and price")
print("Pizza - 12")
print("Burger - 8")
print("Pasta -10")
print("Sandwich -6")
print("Coffee -3")


def price(menu,quantity):
    if quantity <= 0:
        return "Sorry, you can't buy negative numbers"
    if menu not in ["Pizza", "Burger", "Pasta", "Sandwich", "Coffee"]:
        return "Sorry, we dont have that in our menu"
    if menu == "Pizza":
        bill = 12
    elif menu == "Burger":
        bill = 8
    elif menu == "Pasta":
        bill = 10
    elif menu == "Sandwich":
        bill = 6
    elif menu == "Coffee":
        bill = 3
    if quantity > 0:
        total_price = bill * quantity
    if total_price >= 30:
        discount= total_price * 0.10
        final_price = total_price - discount
    else:
        discount = 0
        final_price = total_price
    return bill, total_price, discount,final_price
total_bill = 0
while True:
    choice = input("enter your choice: ")
    quantity =int(input("Enter quantity: "))
    result = price(choice,quantity)
    if result == "Sorry, you can't buy negative numbers" or result == "Sorry, we dont have that in our menu":
        print(result)
    else:
        bill, total_price, discount,final_price = result
        total_bill += total_price
        print("Your price is for one",bill)
        print("Total price is for ",total_price)
        print("Discount",discount)
        print("Final price",final_price)
        print("all total", total_bill)

    choice = input("Do you want another  (yes/no): ")
    if choice.lower() == "no":
        break
