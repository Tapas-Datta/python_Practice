booked_seats = []
total_seats = 5

while True:
    user = input("book the ticket then press 1,see your exiting 2, otherwise 3 ")

    if user == "1":
        print('this is the booked system')
        if len(booked_seats) < total_seats:
            booked_seats.append(input("Enter your name: "))  # 
            print("Successfully Booked!")
        else:
            print("House Full! You cannot book more tickets.")

    elif user == "2":
        print("your ticket name", booked_seats)
        seat_left = total_seats - len(booked_seats)
        print("Seats left:", seat_left)
        if seat_left == 0:
            print("House Full Booked")

    elif user == "3":
        print("Goodbye!")
        break
