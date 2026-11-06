
def hotel_booking(days, room_type, breakfast, extra_guests):
    if days <= 0:
        return "Invalid days"
    elif extra_guests < 0:
        return "Extra guests can not be negative"
    if room_type == "standard":
        booking_room_price = days * 80
    elif room_type == "deluxe":
        booking_room_price = days * 120
    elif room_type == "suite":
        booking_room_price = days * 200
    else:
        return "Invalid room type"
    if breakfast == "yes":
        booking_breakfast_cost = days * 15
    elif breakfast == "no":
        booking_breakfast_cost = 0
    else:
        return "Invalid breakfast"
    booking_extra_guest_cost = days * extra_guests * 20
    booking_final_cost = booking_room_price + booking_breakfast_cost + booking_extra_guest_cost
    return booking_final_cost, booking_room_price, booking_breakfast_cost, booking_extra_guest_cost
user_days = int(input("How many days would you like? "))
user_rooms = input("Which type rooms would you like? ")
user_breakfast = input("Would you like breakfast? ")
user_extra_guests = int(input("How many extra guests would you like to add? "))
result = hotel_booking(user_days, user_rooms, user_breakfast, user_extra_guests)
if isinstance(result, str):
    print(result)
else:
    final_cost, room_price, breakfast_cost, extra_guest_cost = result
    print("Total Costs:", final_cost)
    print("Room Rent:", room_price)
    print("Breakfast Cost:", breakfast_cost)
    print("Extra Guest Cost:", extra_guest_cost)
