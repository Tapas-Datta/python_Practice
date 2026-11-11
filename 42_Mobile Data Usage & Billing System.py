print("Welcome to Mobile Data Usage & Billing System")

while True:
    customer = input("Enter your name: ")
    GB = int(input("Enter your GB: "))
    if GB <= 0:
        print("Invalid data usage")
    else:
        if 0 < GB < 5:
            price = GB * 2
        elif 5 <= GB < 10:
            price = (5 * 2) + ((GB - 5) * 3)
        elif GB >= 10:
            price = (5 * 2) + (5 * 3) + ((GB - 10) * 4)
        if price <= 20:
            discount = 0
        else:
            discount = price * 0.10
        final_bill = price - discount
        print("-------------------------")
        print("Customer:", customer)
        print("Data Usage:", GB, "GB")
        print("Original Bill: €", price)
        print("Discount: €", discount)
        print("Final Bill: €", final_bill)
    user = input("Do you want another time? (yes/no): ")
    if user.lower() == "no":
        break
print("Thank you for using our system!")