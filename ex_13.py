# balance = 5000
# while True:
#     user = int(input("Enter your product: 1.Laptop 2.Phone 3.Headphone 4.Mouse 5.Balance Check 6.Exit: "))
#     if user == 1:
#         if balance >= 3000:
#             balance -= 3000
#             print(f"You bought Laptop. Current balance: {balance}")
#         else:
#             print("Insufficient balance")
#     elif user == 2:
#         if balance >= 2000:
#             balance -= 2000
#             print(f"You bought Phone. Current balance: {balance}")
#         else:
#             print("Insufficient balance")
#     elif user == 3:
#         if balance >= 500:
#             balance -= 500
#             print(f"You bought Headphones. Current balance: {balance}")
#         else:
#             print("Insufficient balance")
#     elif user == 4:
#         if balance >= 200:
#             balance -= 200
#             print(f"You bought Mouse. Current balance: {balance}")
#         else:
#             print("Insufficient balance")
#     elif user == 5:
#         print("Your current balance is:", balance)
#     elif user == 6:
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice")


# def discount_calculator(price):
#     if price >= 5000:
#         discount = price * 0.20
#     elif price >= 3000:
#         discount = price * 0.15
#     elif price >= 1000:
#         discount = price * 0.10
#     elif  0 < price <1000:
#         discount = price * 0
#     else:
#         return "invalid price"
#
#     return discount
# Customer = int(input("Enter your product price: "))
# final_price = discount_calculator(Customer)
# if  final_price == "invalid price":
#     print(final_price)
# else:
#     print("Your product price is",Customer)
#     print("Your discount is : ",final_price)
#     print("your final price is: ",(Customer - final_price))

# total_student = []
# while True:
#     print("1. Add Student")
#     print("2. Remove Student")
#     print("3. Show Total Students")
#     print("4. Exit")
#     user = int(input("Enter as you want to do: "))
#     if user == 1:
#         teacher = input("Enter the name of the Student to add: ")
#         total_student.append(teacher)
#         print(f"Student added successfully! {total_student}")
#     elif user == 2:
#         teacher = input("Enter the name of the student to remove: ")
#         if teacher in total_student:
#             total_student.remove(teacher)
#             print(f"Student remove successfully! {total_student}")
#         else:
#             print("Student not in the list")
#     elif user == 3:
#         print(f"Here are your total students: {total_student}")
#         print("Total number of students:", len(total_student))
#     elif user == 4:
#         print(f"here is your total student: {total_student}")
#         break
#     else:
#         print("Invalid choice!")

# def even_odd(number):
#     if number % 2 == 0:
#         return "the number is even"
#     else:
#         return "the number is odd"
# user = int(input("Enter a number: "))
# print(even_odd(user))


# def multiplication_table(user):
#     for i in range(1,11):
#         total = user * i
#         print(f"{user} x {i} = {total}")
# user = int(input("Enter a number: "))
# multiplication_table(user)

#
# def factorial(number):
#     total = 1
#     for i in range(1, number + 1):
#         total = total * i
#     return total
#
# user_input = int(input("Enter a number: "))
# print(factorial(user_input))

# ===== BANK MANAGEMENT SYSTEM =====
# Choose: 2
# Enter deposit amount: 5000
# Deposit successful!
# Current Balance: 1500
# Choose: 3
# Enter withdraw amount: 2000
# Withdrawal successful!
# Current Balance: 13000
# Choose: 4
# Transaction History:
# Deposit: 5000
# Withdraw: 2000

# balance = 10000
# history = []
#
# def check_balance(balance):
#     return balance
# def deposit(deposit_balance, balance):
#     total_balance_1 = deposit_balance + balance
#     return total_balance_1
# def withdraw(amount, balance):
#     total_balance_2 = balance - amount
#     return total_balance_2
# while True:
#     print("1. Check Balance")
#     print("2. Deposit")
#     print("3. Withdraw")
#     print("4. Transaction History")
#     print("5. Exit")
#     user_choice = int(input("Enter your choice: "))
#     if user_choice == 1:
#         print("Your current balance is:", check_balance(balance))
#     elif user_choice == 2:
#         amount_1 = int(input("Enter your amount: "))
#         if amount_1 <= 0:
#             print("Invalid amount")
#         else:
#             balance = deposit(amount_1, balance)
#             history.append(f"Deposit: {amount_1}")
#             print(f"Deposit amount is successful. Balance: {balance}")
#     elif user_choice == 3:
#         amount_2 = int(input("Enter your amount to withdraw: "))
#         if amount_2 <= 0:
#             print("Invalid amount")
#         elif amount_2 > balance:
#             print("You cannot withdraw more than you have")
#         else:
#             balance = withdraw(amount_2, balance)
#             history.append(f"Withdraw: {amount_2}")
#             print(f"Withdraw amount is successful. Balance: {balance}")
#     elif user_choice == 4:
#         print("History of your transactions:")
#         for i in history:
#             print(i)
#     elif user_choice == 5:
#         print("Your final balance is:", balance)
#         print("Goodbye!")
#         break
#     else:
#         print("Invalid choice!")



