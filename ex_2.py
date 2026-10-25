balance = 0
history = []

while True:
    user = int(input("Enter a number based on your wish (1, 2, 3, 4): "))

    if user == 1:
        amount = int(input("how much do you want deposit: "))
        balance += amount
        print("your balance is", balance)
        history.append(f"Deposited: {amount} TK")
        print("your deposited is", history)

    if user == 2:
        amount = int(input("Enter a balance which you want to withdraw: "))
        if amount <= balance:
            balance -= amount
            print(f"your withdraw now is {amount} and you left {balance}")
            history.append(f"Withdrew: {amount} TK")
            print("your history is", history)
        else:
            print("your withdraw amount is high you only have ", balance)

    if user == 3:
        print(f"your balance is: {balance}")
        print(f"your history is: {history}")

    if user == 4:
        print("Goodbye!")
        break
