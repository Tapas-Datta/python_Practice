
while True:
    user = int(input("Enter your number to check it: "))
    if user > 0:
        print("You have entered a positive number")
    elif user <0:
        print("You have entered a negative number")
    elif user ==0:
        print("You have entered a zero number")
    else:
        print("You have entered an invalid input")

    if user %2==0:
        print("the number is even")
    else:
        print("the number is odd")

    for i in range (1,11):
        print(f"{user} x {i} = {user*i}")

    total = 0
    for digit in str(user):
        total += int(digit)
    print("the total is",total)

    if user == 0:
        break


