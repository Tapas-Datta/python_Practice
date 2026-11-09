

balance = int(input("Enter your starting  balance: "))
while balance >= 0:
    print("Your starting balance is $",balance)
    print("Do you want to deposit, press 1")
    print("Do you want to withdraw, press 2 ")
    print("do you want to check balance, press 3")
    print("do you want to continue your transction, press 4")
    user_choice = input("Enter your choice: ")
    if user_choice == "1":
        amount = int(input("Enter your deposit amount: "))
        if amount <= 0:
            print("Your deposit amount must be positive")
        else:
            balance = balance + amount
            print("your deposit amount is $",amount)
            print("your deposit is successful")
            print("Your total balance is $",balance)
    elif user_choice == "2":
        amount = int(input("Enter your withdrawal amount: "))
        if amount <= 0:
            print("Your withdrawal amount must be positive")
        elif balance >= amount:
            balance = balance - amount
            print("your withdrawal amount is $",amount)
            print("your withdrawal is successful")
            print("Your total balance is $",balance)
        else:
            print("Insufficient Balance")
    elif user_choice == "3":
        print("you total balance is $",balance)
    elif user_choice == "4":
        print("Thank you for using our banking system!")
        break
    else:
        print("invalid input.please chose correct option or contact with bank")

