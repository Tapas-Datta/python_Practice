
# def classify_temperature(temperature):
#         if temperature <= 0:
#             return "freezing"
#         elif 0< temperature  < 15:
#             return "cold"
#         elif 15<= temperature <25:
#             return " mild"
#         else:
#             return "warm"
# user_check_1 =float(input('enter the temperature you want to know'))
# user_check_2 =float(input('enter the temperature you want to know'))
# user_check_3 =float(input('enter the temperature you want to know'))
# print(f"{user_check_1} -> {classify_temperature(user_check_1)}")
# print(f"{user_check_2} -> {classify_temperature(user_check_2)} ")
# print(f"{user_check_3} -> {classify_temperature(user_check_3)} ")
#
#
# def count_positive(values):
#     count = 0
#     for number in values:
#         if number > 0:
#             count += 1
#     return count
# numbers = [4, -2, 0, 7, -1, 5]
# print(count_positive(numbers))
#
# def number(value):
#     total =0
#     count =0
#     highest = value[0]
#     lowest = value[0]
#     for i in value:
#         total +=
#         count+=1
#         if i>highest:
#             highest = i
#         if i<lowest:
#             lowest =
#     return (total /count),highest,lowest
# values = [18, 12, 25, 7, 20]
# final_avg,high,low =number(values)
# print(final_avg)
# print(high)
# print(low)
#
# def check_vowel(letter):
#     vowel =["a","e","i","o","u"]
#     count = 0
#     for word in letter:
#         if word.lowe() in vowel:
#             count +=1
#     return count
# user =input("Enter a word: ")
# total_vowel=check_vowel(user)
# print(total_vowel)
#
# def is_palindrome(text):
#     if text == text[::-1]:
#         return True
#     return False
# user=input("Enter a the word: ")
# print(is_palindrome(user))

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












