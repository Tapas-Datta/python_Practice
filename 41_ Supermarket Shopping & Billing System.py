customer=  input("Enter your name:")
print("please select your product")
print("Rice Per KG 5 euro")
print("Milk per litre 2 euro")
print("Bread per packet 3 euro")
print("Eggs per dozen 4 euro")
print("Chicken per kg 8 euro ")
total = 0
grand_total = 0
while True:
    choice = int(input("please enter your product choice? : "))
    quantity = int(input("How many items do you want? "))

    if quantity <= 0:
        print("Sorry, quantity must be positive")
        continue
    if choice not in [1,2,3,4,5]:
        print("sorry, we dont have that product")
        continue

    if choice == 1:
        price = quantity * 5
        total += price
        grand_total += price
        print("rice = 5 euro" )
        print("Your total price is $",price)

    elif choice == 2:
        price = quantity * 2
        total += price
        grand_total += price
        print("Milk = 2 euro" )
        print("Your total price is $",price)

    elif choice == 3:
        price = quantity * 3
        total += price
        grand_total += price
        print("Bread = 3 euro" )
        print("Your total price is $",price)

    elif choice ==4:
        price = quantity * 4
        total += price
        grand_total += price
        print("Eggs = 4 euro" )
        print("Your total price is $",price)

    elif choice ==5:
        price = quantity * 8
        total += price
        grand_total += price
        print("chicken = 8 euro" )
        print("Your total price is $",price)
    user = input("Do you want another product? (yes/no): ")
    if user.lower() == "no":
        break

if total < 50:
    discount = 0
elif 50 <= total < 100:
    discount = total * 0.05
elif 100 <= total < 200:
    discount = total * 0.10
else:
    discount = total * 0.15

final_bill = total - discount

print("-------------------------")
print("Customer:", customer)
print("Grand Total:", total)
print("Discount:", discount)
print("Final Bill:", final_bill)
print("Goodbye!")




        
        

