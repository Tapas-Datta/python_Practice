def hotel_booking(room,nights,breakfast):
    while True:
        room_type = ["standard","deluxe","premium"]
        if room not in room_type:
            return "Invalid room"
        elif nights <= 0:
            return "Invalid nights"
        elif breakfast not in ["yes","no"]:
            return "Invalid breakfast input"
        if room == "standard":
            room_price = 50
        elif room == "deluxe":
            room_price = 80
        elif room == "premium":
            room_price = 120
        if nights < 3:
            discount = 0
        elif nights >= 3:
            discount = 0.10
        if breakfast == "yes":
            breakfast_price =(nights * 10)
        elif breakfast == "no":
            breakfast_price = 0
        room_cost = room_price * nights
        total_cost = room_cost + breakfast_price
        room_discount = total_cost * discount
        final_price = breakfast_price + room_cost - room_discount
        return room_cost,breakfast_price,total_cost,room_discount, final_price

print("standard","deluxe","premium")
user=input("enter the room type:")
nights_user = int(input("enter the number of nights:"))
breakfast_user = input("do you want the breakfast:")
result = hotel_booking(user,nights_user,breakfast_user)
if result == "Invalid room" or result == "Invalid nights" or result == "Invalid breakfast input":
    print(result)
else:
    room_cost, breakfast_price, total_cost, room_discount, final_price = result
    print("room_cost:", room_cost)
    print("breakfast_price:", breakfast_price)
    print("total_cost:", total_cost)
    print("discount:", room_discount)
    print("final_price:", final_price)








