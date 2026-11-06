def flight_booking(ticket_price, passengers, seat_type, baggage_kg):
    if ticket_price <= 0:
        return "Invalid Price"
    elif passengers <= 0:
        return "Invalid Passengers"
    elif baggage_kg < 0:
        return "Invalid Baggage"
    passenger_price = ticket_price * passengers
    if seat_type == "business":
        total_ticket = 500 * passengers
    elif seat_type == "first":
        total_ticket = 1000 * passengers
    elif seat_type == "economy":
        total_ticket = 0
    else:
        return "Invalid Seat Type"
    if baggage_kg <= 20:
        total_kg = 0
    elif baggage_kg > 20:
        baggage_kg -= 20
        total_kg = baggage_kg * 10 * passengers
    final_cost = passenger_price + total_ticket + total_kg
    return passenger_price, total_ticket, total_kg, final_cost
user = int(input("Enter your ticket price: "))
passengers_1 = int(input("Enter number of passengers: "))
seat_type_1 = input("Enter seat type: ")
baggage_kg_1 = int(input("Enter baggage kg: "))
result = flight_booking(user, passengers_1, seat_type_1, baggage_kg_1)
if isinstance(result, str):
    print(result)
else:
    passenger_price, total_ticket, total_kg, final_cost = result
    print("Ticket Total:", passenger_price)
    print("Seat Charge:", total_ticket)
    print("Baggage Charge:", total_kg)
    print("Final Amount:", final_cost)



