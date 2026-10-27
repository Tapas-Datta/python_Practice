
def classify_temperature(temperature):
        if temperature <= 0:
            return "freezing"
        elif 0< temperature  < 15:
            return "cold"
        elif 15<= temperature <25:
            return " mild"
        else:
            return "warm"
user_check_1 =float(input('enter the temperature you want to know'))
user_check_2 =float(input('enter the temperature you want to know'))
user_check_3 =float(input('enter the temperature you want to know'))
print(f"{user_check_1} -> {classify_temperature(user_check_1)}")
print(f"{user_check_2} -> {classify_temperature(user_check_2)} ")
print(f"{user_check_3} -> {classify_temperature(user_check_3)} ")


def count_positive(values):
    count = 0
    for number in values:
        if number > 0:
            count += 1
    return count
numbers = [4, -2, 0, 7, -1, 5]
print(count_positive(numbers))

def number(value):
    total =0
    count =0
    highest = value[0]
    lowest = value[0]
    for i in value:
        total +=
        count+=1
        if i>highest:
            highest = i
        if i<lowest:
            lowest =
    return (total /count),highest,lowest
values = [18, 12, 25, 7, 20]
final_avg,high,low =number(values)
print(final_avg)
print(high)
print(low)

def check_vowel(letter):
    vowel =["a","e","i","o","u"]
    count = 0
    for word in letter:
        if word.lowe() in vowel:
            count +=1
    return count
user =input("Enter a word: ")
total_vowel=check_vowel(user)
print(total_vowel)

def is_palindrome(text):
    if text == text[::-1]:
        return True
    return False
user=input("Enter a the word: ")
print(is_palindrome(user))

def sumar (num1, num2):
    return num1 + num2
num3= 5
num4 = 3
print(sumar(num3, num3))

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False
student = is_even(8)
print(student)


def check_bigger(a,b):
    return max(a,b)
student_1 = check_bigger(4,5)
student_2 = check_bigger(10,4)
print(student_1)
print(student_2)

user = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{user} x {i} = {user * i}")


def table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")
user_1= int(input("Enter a number: "))
table(user_1)












# practice
