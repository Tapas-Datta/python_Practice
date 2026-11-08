total_seat = 10
booked_seat = []
count =0
price =12
print("Welcome to Cinema Booking System")
while True:
    print("Do want to book the seat,then 1 ?")
    print("do you want exit,then 5?")
    user_choice = int(input("Enter your choice: "))
    if user_choice == 1:
        number_of_seats = int(input("Enter number of seats: "))
        if number_of_seats < 1 or number_of_seats > total_seat:
            print("Invalid seat number")
        elif number_of_seats in booked_seat:
            print("seat is already booked")
        else:
            booked_seat.append(number_of_seats)
            count += 1
            print(f"your seat is booked successfully. your seat number is: {number_of_seats}")

            total_price = price * count

            if count >= 3:
                discount = total_price * 0.10
                total_price_1 = total_price - discount
                print("your total price is:", total_price_1)
            else:
                print("your total price is:", total_price)
    elif user_choice == 5:
        print("Goodbye!")
        break