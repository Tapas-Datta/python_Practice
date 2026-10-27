

username_1 = None
password_1 = None
balance = 0
customer = int(input("Do you want to sign up then press (1) or sign in the account (2) and check the stuff 3 : "))
if customer == 1:
    username_1 =input("create your username : ").lower()
    password_1 =int(input("Enter your password : "))
    print("congratulation! you are signed up.press 2 to access your account")
    customer = 2

while True:
    if customer == 2:
        print("your are now sign in page! put your username and password ")
        username_2 =input("Enter your username : ").lower()
        password_2= int(input("Enter your password : "))
        if username_2 != username_1:
            print("wrong username")
        elif password_2 !=  password_1:
            print("wrong password")
        else:
            print("you are signed in.")
            customer = 3
    while True:
        if customer == 3:
            customer_3= int(input("Enter what you want to do.do you want to deposit/withdraw/check_balance?close_account : "))
            if customer_3 == 1:
                amount = int(input("Enter how much you want to deposit : "))
                balance += amount
                print(f"you have deposited{amount} and your balance is {balance}")
            elif customer_3 == 2:
                withdraw_amount = int(input("Enter how much you want to withdraw : "))
                balance -= withdraw_amount
                print(f"you have withdrawn {withdraw_amount} and your balance is {balance}")
            elif customer_3 == 3:
                print(f"your total balance is {balance}")
            elif customer_3 == 4:
                print(f"Good Bye{username_1}! stay connected with us")
                exit()





