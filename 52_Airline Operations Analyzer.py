
airline_employee_name=input("Enter your  name")
quantity_of_flight_record = int(input("Enter the number of flight record: "))
f_ID=[]
destiny = []
total_ticket_prices = []
total_seats = []
total_booked_seats = []
total_cancel_seats = []
for number_of_flight in range(quantity_of_flight_record):
    flight_ID = int(input("Enter flight ID: "))
    f_ID.append(flight_ID)
    destination = input("Enter your  destination: ")
    destiny.append(destination)
    ticket_price = int(input("Enter your ticket price: "))
    total_ticket_prices.append(ticket_price)
    seat = int(input("Enter your total seats: "))
    total_seats.append(seat)
    booked_seats = int(input("Enter your booked seats: "))
    total_booked_seats.append(booked_seats)
    cancel_seats = int(input("Enter your cancel seats: "))
    total_cancel_seats.append(cancel_seats)
def calculate_revenue(total_ticket_prices, total_booked_seats):
    revenue_list = []
    total_revenue = 0
    for i in range (len(total_ticket_prices)):
        revenue = total_booked_seats[i] * total_ticket_prices[i]
        revenue_list.append(revenue)
        total_revenue += revenue
    return revenue_list, total_revenue
def analyze_occupancy(total_booked_seats,total_seats ):
    occupancy_list = []
    total_occupancy = 0
    for i in range (len(total_seats)):
        occupancy = (total_booked_seats[i] / total_seats[i] ) * 100
        occupancy_list.append(occupancy)
        total_occupancy += occupancy
    average_occupancy = total_occupancy / len(total_booked_seats)
    highest_occupancy = max(occupancy_list)
    lowest_occupancy = min(occupancy_list)
    return average_occupancy, highest_occupancy, lowest_occupancy, occupancy_list


def analyze_flights(f_ID, total_cancel_seats, quantity_of_flight_record, total_booked_seats, total_seats, total_ticket_prices):
    total_available_seats = 0
    total_booked = 0
    for i in range(len(total_seats)):
        total_available_seats += total_seats[i] - total_booked_seats[i]
        total_booked += total_booked_seats[i]
    most_profitable = total_booked_seats[0] * total_ticket_prices[0]
    most_profitable_flight = f_ID[0]
    for i in range(len(total_ticket_prices)):
        profitable_flight = total_booked_seats[i] * total_ticket_prices[i]
        if profitable_flight > most_profitable:
            most_profitable = profitable_flight
            most_profitable_flight = f_ID[i]
    least_profitable = total_booked_seats[0] * total_ticket_prices[0]
    least_profitable_flight = f_ID[0]
    for i in range(len(total_ticket_prices)):
        profitable_flight = total_booked_seats[i] * total_ticket_prices[i]
        if profitable_flight < least_profitable:
            least_profitable = profitable_flight
            least_profitable_flight = f_ID[i]
    highest_occupancy = (total_booked_seats[0] / total_seats[0]) * 100
    highest_occupancy_flight = f_ID[0]
    lowest_occupancy = (total_booked_seats[0] / total_seats[0]) * 100
    lowest_occupancy_flight = f_ID[0]
    for i in range(len(total_seats)):
        occupancy = (total_booked_seats[i] / total_seats[i]) * 100
        if occupancy > highest_occupancy:
            highest_occupancy = occupancy
            highest_occupancy_flight = f_ID[i]
        if occupancy < lowest_occupancy:
            lowest_occupancy = occupancy
            lowest_occupancy_flight = f_ID[i]
    return quantity_of_flight_record, total_available_seats, total_booked, most_profitable_flight, least_profitable_flight, highest_occupancy_flight, lowest_occupancy_flight
def classify_flights(occupancy_list):
    performance_list = []
    for occupancy in occupancy_list:
        if occupancy >= 90:
            performance = "Excellent"
        elif occupancy >= 70:
            performance = "Good"
        elif occupancy >= 40:
            performance = "Average"
        else:
            performance = "Poor"
        performance_list.append(performance)
    return performance_list
average_occupancy, highest_occupancy, lowest_occupancy, occupancy_list = analyze_occupancy(total_booked_seats, total_seats)

performance_list = classify_flights(occupancy_list)

print("Average Occupancy:", average_occupancy)
print("Highest Occupancy:", highest_occupancy)
print("Lowest Occupancy:", lowest_occupancy)
print("Flight Performance:", performance_list)