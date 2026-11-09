while True:
    password= input("Enter your password: ")
    is_strong = True

    if len(password) < 8:
        print("password is too short")
        is_strong = False

    if len(password) >= 8:
        if password == password.upper():
            print("password has no lower case letters")
            is_strong = False

        if password == password.lower():
            print("password has no upper case letters")
            is_strong = False

        if "@" not in password and "#" not in password and "$" not in password and "!" not in password:
            print("Password has no special characters")
            is_strong = False

        if not any(number in password for number in "0123456789"):
            print("Password has no number")
            is_strong = False

    if is_strong:
        print("your password is enough is strong")
    else:
        print("your password is weak")

    choice = input("Do you want to check another password? (yes/no): ")
    if choice == "no":
        break