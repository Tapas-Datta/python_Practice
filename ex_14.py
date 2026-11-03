
def shopping_bill(price, quantity):
    if price <= 0 or quantity <= 0:
        return "invalid price"
    total_price = price * quantity

    if total_price >= 5000:
        discount = total_price * 0.20
        final_bill = total_price - discount
    elif total_price >= 3000:
        discount = total_price * 0.15
        final_bill = total_price - discount
    elif total_price >= 1000:
        discount = total_price * 0.10
        final_bill = total_price - discount
    else:
        discount = total_price * 0
        final_bill = total_price - discount
    return final_bill
quantity_1 = int(input("Enter the quantity of the user: "))
per_price = int(input("Enter the price of the product: "))

final_bil_1 = shopping_bill(per_price, quantity_1)

if final_bil_1 == "invalid price":
    print(final_bil_1)
else:
    product_price = per_price * quantity_1
    print("your product price is", product_price)
    print(f"your discount is {product_price - final_bil_1}")
    print("your final bill is", final_bil_1)

1. তিনটি Subject-এর Total Marks বের করবে।
2. Average Marks বের করবে।
3. Average 90 বা বেশি হলে → A+
4. Average 80 বা বেশি হলে → A
5. Average 70 বা বেশি হলে → B
6. Average 60 বা বেশি হলে → C
7. Average 40 বা বেশি হলে → D
8. Average 40-এর কম হলে → Fail।
9. কোনো Subject-এর Marks 0-এর কম বা 100-এর বেশি হলে → Invalid Marks।
Example:
Enter Math marks: 90
Enter English marks: 80
Enter Science marks: 70
Total Marks: 240
Average: 80
Grade: A

def student_result(math, english, science):
    total_marks = math + english + science
    avg_marks = total_marks / 3
    if avg_marks >= 90:
        return "A+"
    elif avg_marks >= 80:
        return "B"
    elif avg_marks >= 70:
        return "C"
    elif avg_marks >= 60:
        return "D"
    elif avg_marks >= 40:
        return "E"
    elif avg_marks < 40:
        return "F"

Math_1 =int(input("Enter your math marks"))
English_1 =int(input("Enter your english marks" ))
Science_1 =int(input("Enter your science marks" ))
print("Average:" ,(Math_1 + English_1 + Science_1)/3 )
print("Grade",student_result(Math_1, English_1, Science_1))

def calculate_salary(basic_salary, bonus, tax):
    gross_salary = basic_salary + bonus
    net_salary =  gross_salary - tax
    if net_salary >= 50000:
        return "High Salary"
    elif net_salary >= 30000:
        return "Medium Salary"
    else:
        return "Low Salary"

user_1_basic = int(input("basic salary: "))
user_1_bonus = int(input(" Enter your Bonus "))
user_1_tax = int(input("Enter your tax: "))
print("Basic :", user_1_basic)
print("Bonus :",user_1_bonus)
print("Tax :", user_1_tax)
print("Salary Category:",(calculate_salary(user_1_basic, user_1_bonus, user_1_tax)))

deposit হলে balance-এর সঙ্গে amount যোগ করবে।
withdraw হলে balance থেকে amount দেবে।
Insufficient balance হলে "Insufficient Balance" return করব
Invalid transaction হলে "Invalid Transaction" return করবে।
Negative amount হলে "Invalid Amount" return করবে।
Updated balance return

def bank_account(balance, transaction_type, amount):
    if amount <= 0:
        return "Invalid Amount"
    elif transaction_type == "deposit":
        deposit = balance + amount
        return deposit
    elif transaction_type == "withdraw":
        if amount > balance:
            return "Insufficient Balance"
        else:
            withdraw = balance - amount
            return withdraw
    else:
        return "Invalid Transaction"

user_balance = int(input("Enter your balance: "))
user_transaction = input("Enter transaction type: ")
user_amount = int(input("Enter amount: "))
result = bank_account(user_balance, user_transaction, user_amount)
print("Updated Balance:", result)



def employee_bonus(salary, experience, performance):
    if experience >= 5 and performance =="excellent":
        bonus = salary * 0.20
        total_salary = salary + bonus
        return total_salary
    elif experience >=3 and performance =="good":
        bonus = salary * 0.10
        total_salary = salary + bonus
        return total_salary
    elif experience >= 1:
        bonus = salary * 0.05
        total_salary = salary + bonus
        return total_salary
    else:
        return salary
user_salary = int(input("Enter your salary: "))
user_performance = input("Enter your performance: ").lower()
user_year = int(input("Enter your years: "))
final_decision = employee_bonus(user_salary, user_year, user_performance)
print("bonus: ",(final_decision - user_salary))
print("Final Salary:", final_decision)

একটি list-এর মধ্যে একাধিক product price থাকবে।
সব product-এর total price বের করবে।
Total price 1000 বা বেশি হলে 10% discount।
Total price 500 বা বেশি হলে 5% discount।
500-এর কম হলে কোনো discount নেই।
Final amount return

def shopping_discount(prices):
    total_price = sum(prices)
    if total_price >=1000:
        discount_price = total_price * 0.10
        total_amount = total_price - discount_price
        return total_amount
    elif total_price >=500:
        discount_price = total_price * 0.05
        total_amount = total_price - discount_price
        return total_amount
    else:
        return total_price

user_1 =int(input("Enter the product pirce  did you buy"))
user_2 =int(input("Enter the product pirce  did you buy"))
user_3 =int(input("Enter the product pirce  did you buy"))
total_price = user_1 + user_2 + user_3
final_amount = shopping_discount([user_1,user_2,user_3])
print("The total amount is",total_price)
print("the discount is",(total_price - final_amount))
print("The final amount is ",final_amount)





