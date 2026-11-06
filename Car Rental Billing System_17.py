def car_rental(days, car_type, insurance, extra_km):
    if days <= 0:
        return "Invalid days"
    if car_type == "economy":
        price_day = 50 * days
    elif car_type == "standard":
        price_day = 80 *days
    elif car_type == "luxury":
        price_day = 120 * days
    else:
        return "Invalid car type"
    if insurance  == "yes":
        insurance_price =  20 * days
    else:
        insurance_price = 0 * days
    if extra_km < 0:
        return "Invalid distance"
    elif extra_km <= 100:
        extra_km = 0
        extra_km_price = extra_km + 0
    elif extra_km > 100:
        extra_km -= 100
        extra_km_price = extra_km * 2
    final_amount = (price_day + insurance_price + extra_km_price)
    return price_day,final_amount, insurance_price,extra_km_price

user_days = int(input("Enter how many days: "))
user_car_type = input("Enter car type: ")
user_insurance = input("Enter insurance: ")
user_extra_km = int(input("Enter extra km: "))
result = car_rental(user_days, user_car_type, user_insurance, user_extra_km)
if isinstance(result, str):
    print(result)
else:
    price_day,final_amount, insurance_price,extra_km_price = result
    print("Car rent: ", price_day)
    print("Final Amount: ", final_amount)
    print("Insurance: ", insurance_price)
    print("Extra Km: ", extra_km_price)
