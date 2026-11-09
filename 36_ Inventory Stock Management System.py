
transaction = 0
while True:
    user = input("Enter the product name: ")
    quantity= int(input("Enter the product quantity "))
    sold_quantity =int(input("Enter the sold quantity "))
    previous_stock = quantity
    if quantity == 0:
        print("Product is out of stock")
    elif sold_quantity == 0:
        print("No sale")
    elif sold_quantity <= quantity:
        quantity -= sold_quantity
        transaction += 1
        print(f"sold quantity: {sold_quantity}")
        print("Transaction", transaction)
    else:
        print("Product not available")
    print("Previous Stock", previous_stock)
    print("Remaining Stock", quantity)
    if quantity == 0:
        print("Out of Stock")
    choice = input("Do you want another transaction? (yes/no): ")
    if choice == "no":
        break







