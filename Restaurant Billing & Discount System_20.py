

def restaurant_bill(food_amount, customers, discount):
    if food_amount <= 0:
        return "invalid amount"
    service_charge = food_amount * 0.10
    if discount == "yes":
        food_amount_discount = food_amount * 0.15
    elif discount == "no":
        food_amount_discount = food_amount * 0
    else:
        return "invalid discount"
    if customers <= 0:
        return "invalid customers"
    elif customers <= 5 :
        customers_extra_charge = 0
    elif customers > 5:
        customers_charge = customers - 5
        customers_extra_charge = customers_charge * 20
    final_amount = food_amount - food_amount_discount + service_charge + customers_extra_charge
    return  food_amount,service_charge,food_amount_discount,customers_extra_charge, final_amount

user_food_amount = int(input("Enter your food amount: "))
customers = int(input("Enter how many customers: "))
discount = input("Enter your discount: ")
result = restaurant_bill(user_food_amount, customers, discount)
if result == "invalid amount" or result == "invalid discount" or result == "invalid customers":
    print(result)
else:
    food_amount, service_charge, food_amount_discount, customers_extra_charge, final_amount = result
    print("food amount:", food_amount)
    print("service charge", service_charge)
    print("customer discount", food_amount_discount)
    print("customer extra_charge", customers_extra_charge)
    print("final amount", final_amount)
    

