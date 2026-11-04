
def basic_salary(salary):
    if salary >= 5000:
        bonus = salary * 0.20
        total_salary =  salary + bonus
        return total_salary
    elif salary >= 3000:
        bonus = salary * 0.10
        total_salary = salary + bonus
        return total_salary
    else:
        bonus = salary * 0.05
        total_salary = salary + bonus
        return total_salary
user=  int(input("enter your salary"))
print(basic_salary(user))

def student_grade(marks):
    if marks >= 90:
        return "A +"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 40:
        return "D"
    else:
        return "Fail"
print(student_grade(90))
print(student_grade(80))
print(student_grade(70))


def electricity_bill(units):
    if units <= 100:
        total = units * 5
    elif units <= 200:
        total = (100 * 5) + ((units - 100) * 7)
    else:
        total = (100 * 5) + (100 * 7) + ((units - 200) * 10)
    return total
print(electricity_bill(80))
print(electricity_bill(150))
print(electricity_bill(250))


def shopping_discount(price,quantity):
    total_price = price * quantity
    if total_price >= 5000:
        total_price_discount = total_price -(total_price * 0.20)
        return total_price_discount
    elif total_price >= 3000:
        total_price_discount = total_price -(total_price * 0.15)
        return total_price_discount
    elif total_price >= 1000:
        total_price_discount = total_price -(total_price * 0.10)
        return total_price_discount
    else:
        return total_price
user_price = int(input("Enter the price of the product: "))
user_quantity = int(input("Enter the quantity of the product:"))
Discounted_Price = shopping_discount(user_price,user_quantity)
print("Original Price:", user_price*user_quantity)
print(f"Discount: {(user_price * user_quantity) -Discounted_Price}")
print("Final Price:", Discounted_Price)


def hotel_booking(room_price, nights, guests):
    total_room_price = room_price * nights
    if guests == 1:
        return total_room_price
    elif guests == 2:
        extra_charge = total_room_price * 0.10
        total_price = total_room_price + extra_charge
        return total_price
    elif guests >= 3:
        extra_charge = total_room_price * 0.20
        total_price = total_room_price + extra_charge
        return total_price
    else:
        return "invalid input"

user_room_price = int(input("Enter room price: "))
user_nights = int(input("Enter number of nights: "))
user_guests = int(input("Enter number of guests: "))
Final_price = (hotel_booking(user_room_price, user_nights, user_guests))
print(f"Room Costs: {user_room_price * user_nights}")
print(f"extra charge : {Final_price -(user_nights * user_room_price)}")
print("Final_price",Final_price)


def mobile_data_bill(data_gb, price_per_gb, extra_gb):
    total_price  = data_gb * price_per_gb
    if data_gb <= 5:
        discount =0
    elif data_gb <=10:
        discount = total_price * 0.10
    else:
        discount = total_price * 0.20
    extra_charge = extra_gb * 50
    final_price = total_price - discount + extra_charge
    return final_price


user=int(input("Enter your data_gb: "))
user_1 = int(input("Enter your price_per_gb: "))
user_2 = int(input("Enter your extra_gb: "))
original_price = (user * user_1)
final_bill = mobile_data_bill(user, user_1, user_2)
discount_1 = original_price * 0.20
print("Original Price is ",original_price)
print("Discount is ",discount_1)
print("Final Bill is ",final_bill)







