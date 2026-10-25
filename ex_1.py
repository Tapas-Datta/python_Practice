def check_password(password_list):
    for password in password_list:
        if len(password) >= 6 and "@" in password:
            print("your password is strong")
        else:
            print("your password is wrong")
user = [input('enter your password ')]
check_password(user)


def check_email(email_list):
    for email in email_list:
        if "@" in email:
            print("your email is valid")
        else:
            print("your email is not valid")
user =  [input("Enter your email:")]
check_email(user)

def checkemail(email):
    for correct in email:
        if correct.endswith(".com"):
            print(correct)
        else:
            print("try again")
user = [input("enter your username")]
checkemail(user)


def check_email(emails):
    for email  in emails:
        if email.startswith("Tapas".lower()) and email.endswith("com".lower()):
            print (f"Email found : {email}" )
        else:
            print("Email not found.Try again")
user = [input("Enter your username: ")]
check_email(user)

def sum_numbers(numbers_list):
    total_number = 0
    for total in numbers_list:
        total_number += total
    return total_number
all_numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final_sum = sum_numbers(all_numbers_list)
print(final_sum)