print("Welcome to ATM")
print ("Check Balance /1")
print("Deposit Money /2")
print("Withdraw Money /3")
print("Exit /4")
balance = 10000
while True:
    user = int(input("enter your choice:"))
    if user == 1:
       print("Your Balance is:",balance)
    elif user == 2:
        amount = int(input("enter the amount to deposit:"))
        if amount > 0 :
            balance = balance + amount
            print(f"Your deposit is successful! ")
            print("new balance",balance)
        else:
            print("Your deposit is failed  bcz you put wrong amount ")
    elif user == 3:
        amount = int(input("enter the amount to withdraw:"))
        if amount > 0 and balance >= amount:
           balance = balance - amount
           print(f"your withdraw is successful! ")
           print("new balance",balance)
        else:
           print("your withdraw is failed  bcz you put wrong amount ")
    elif user == 4:
        print("Thank you for using ATM!")
        break

