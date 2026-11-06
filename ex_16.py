


def employee_bonus(salary, performance_rating, years_of_experience):
    if performance_rating < 1 or performance_rating > 5:
        return "Invalid Rating"
    if performance_rating == 5:
        performance_salary = salary * 0.20
    elif performance_rating == 4:
        performance_salary= salary * 0.15
    elif performance_rating == 3:
        performance_salary = salary * 0.10
    elif performance_rating < 3:
        performance_salary = 0
    else:
        performance_salary = 0
    if years_of_experience >= 5:
        experience_salary = salary * 0.05
    else:
        experience_salary = 0
    final_salary =performance_salary + experience_salary + salary
    return performance_salary, experience_salary ,final_salary

user_salary = int(input("Enter salary: "))
user_rating = int(input("Enter performance rating: "))
user_experience = int(input("Enter experience: "))
performance_salary, experience_salary, final_salary = employee_bonus(user_salary, user_rating, user_experience)
print("Basic Salary:", user_salary)
print("Final Salary:", final_salary)

def order_calculator(price, quantity, delivery_type, coupon):
    total_price = price * quantity
    if coupon == "save10":
        discount = total_price * 0.10
    elif coupon == "save20":
        discount =  (total_price * 0.20)
    elif coupon == "save30":
        discount =(total_price * 0.30)
    else:
        return "Invalid Input"
    if delivery_type == "express":
        delivery_cost =  100
    elif delivery_type == "normal":
        delivery_cost =  50
    elif delivery_type == "free":
        delivery_cost = 0
    else:
        return "invalid delivery type"
    final_price = total_price - discount + delivery_cost
    return final_price, discount, delivery_cost

user_price = int(input("Enter your price: "))
user_quantity = int(input("Enter your quantity: "))
user_delivery_type = input("Enter your delivery type: ")
user_coupon = input("Enter your coupon: ")
result = order_calculator(user_price, user_quantity, user_delivery_type, user_coupon)

if result == "Invalid Input" or result == "invalid delivery type":
    print(result)
else:
    final_price, discount, delivery_cost = result

    print("Original Price:", user_price * user_quantity)
    print("Discount:", discount)
    print("Delivery Charge:", delivery_cost)
    print("Final Amount:", final_price)



