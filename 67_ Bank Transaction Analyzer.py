balance  = int(input("enter the starting balance: "))
transaction = int(input("Enter how many transaction you want to do: "))
total_deposit = 0
deposit_list = []
deposit_count = 0
total_withdrawl = 0
withdraw_list = []
withdraw_count = 0
insufficient_try = 0

for i in range(transaction):
    type_of_transaction = input("enter what type of transaction you want to do: ")
    if type_of_transaction.lower() == "deposit" or type_of_transaction.lower() == "d":
        amount = int(input("enter the amount you want to deposit: "))
        deposit_list.append(amount)
        total_deposit += amount
        balance += amount
        deposit_count += 1
    elif type_of_transaction.lower() == "withdraw" or type_of_transaction.lower() == "w":
        amount = int(input("enter the amount you want to withdraw: "))
        if balance >= amount:
            withdraw_list.append(amount)
            total_withdrawl += amount
            balance -= amount
            withdraw_count += 1
        else:
            insufficient_try += 1
            

print("====================================")
print("final balance: ", balance)
print("====================================")
print("total deposit: ", total_deposit)
print("here is your list for you all list: ", deposit_list)
print("here is how many deposit you did: ", deposit_count)
print("====================================")
print("total withdrawl: ", total_withdrawl)
print("here is your list for you all list: ", withdraw_list)
print("here is how many withdraw you did: ", withdraw_count)
print("=====================================")
print("here is your insufficient try: ", insufficient_try)


