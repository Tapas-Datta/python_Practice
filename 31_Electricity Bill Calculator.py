def electricity_bill(unit):
    if unit <= 100:
        total = unit * 0.10
    elif unit <= 200:
        total = (100 * 0.10) + ((unit - 100) * 0.15)
    else:
        total = (100 * 0.10) + (100 * 0.15) + ((unit - 200) * 0.20)
    if total > 30:
        discount = total * 0.05
    else:
        discount = 0

    final_bill = total - discount
    return total, discount, final_bill
while True:
    user = input("Enter electricity units or exit: ")
    if user.lower() == "exit":
        print("Goodbye!")
        break
    unit = int(user)
    if unit < 0:
        print("Invalid input")
    else:
        total, discount, final_bill = electricity_bill(unit)
        print("Total Bill:", total)
        print("Discount:", discount)
        print("Final Bill:", final_bill)