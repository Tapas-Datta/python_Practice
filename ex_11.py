
def score(values):
    return values
def average(values):
    total_marks = 0
    total_student = 0
    for number in values:
        total_marks = total_marks + number
        total_student += 1
    average_marks = total_marks / total_student
    return average_marks
def count_passed(values):
    count_1 = 0
    for number in values:
        passed_marks = 18
        if number >= passed_marks:
            count_1 += 1
    return  count_1
def best_score(values):
    best_secore = values[0]
    for number in values:
        if number > best_secore:
            best_secore= number
    return best_secore
def passed_scores(values):
    passed_score = []
    passed_marks = 18
    for number in values:
        if number >= passed_marks:
            passed_score.append(number)
    return passed_score



scores = [23, 18, 27, 14, 30, 21, 17, 25]
print(f"scores: {score(scores)}")
print(f"Best Score: {best_score(scores)}")
print(f"Average: {average( scores)}")
print(f"Passed {count_passed(scores)}")
print(f"Best: {best_score(scores)}")
print(f"Passing scores: {passed_scores(scores)}")

def square(x):
    return x * x
print(square(4))

def maximum(a, b):
   if a > b:
       return a
   else:
       return b
x = maximum(5, 9)
# print(x)

values = [4, 8, 12]
for i in range(len(values)):
    print(values[i])

text = "python"
text_1 = "P" + text[1:]
print(text_1)




def calculate_invoice(cart):
    if len(cart) == 0:
        return 0
    total_price = 0
    for number in cart:
        if number > 100:
            total_price += number - (number / 10)
        elif number <= 100:
            total_price += number
    if total_price >= 500:
        print("you have free deliver")
        return total_price
    else:
        delivery_charge = total_price + 50
        print(delivery_charge)
        return delivery_charge
cart_items = [50, 120, 200, 30]
calculate_invoice(cart_items)






