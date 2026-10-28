def odd(limit):
    total = 0
    for number in range (1,limit+1):
        if number % 2 != 0:
            total += number
    return total
print(odd(50))


def vowel(word):
    total = 0
    for letter in word:
        if letter in ("a", "e", "i", "o", "u"):
            total += 1
    return total
print(vowel("hey ,this is  tapas"))
print(vowel("programming"))
print(vowel("world"))


def user(number):
    total = 1
    for number_1 in range(1,number+1):
        total = total * number_1
    return total
print(user(10))


def revers_word(word):
    return word[::-1]
print(revers_word("Hello"))
print(revers_word("World"))


def reverse_word(word):
    if word == word[::-1]:
        return word
    else:
        return "not a reverse word"
user= input("Palindrome checker ")
print(reverse_word(user))

def max_number(number):
    return max(number)
user = [3, 8, 1, 15, 7]
print (max_number(user))


def uni(number):
    return set(number)
print(uni([1, 2, 2, 3, 4, 4, 5]))

def uni_number(number):
    uni_number_1= []
    for uni_number_2 in number:
        if uni_number_2 not in uni_number_1:
            uni_number_1.append(uni_number_2)
    return uni_number_1
user = [3, 8, 1, 15, 7,9,3,9,15]
print(uni_number(user))


def challenge(number):
    if number %3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return number
user_guess = int(input("Enter your guess: "))
print(challenge(user_guess))

grocery_prices = {"apple": 120, "banana": 40, "orange": 80}
def checking(item):
    if item in grocery_prices:
        return grocery_prices[item]
    else:
        return "product not found"
user = input("Enter your product name: ")
print(checking(user))


def checking_year(year):
    if year % 400 == 0:
        return "Yes, that is a leap year!"
    elif year % 100 == 0:
        return "Not a leap year!"
    elif year % 4 == 0:
        return "Yes, that is a leap year!"
    else:
        return "Not a leap year!"

user = int(input("Enter a year: "))
print(checking_year(user))


def avg_number(number):
    return sum(number) / len(number)
user = [10, 20, 30, 40,12]
print(avg_number(user))

def avg_number(number):
    total_number =0
    count = 0
    for number_1 in number:
        total_number = total_number + number_1
        count = count + 1
    return total_number/count
user = [10, 20, 30, 40,12]
print(avg_number(user))

def checking_word(word):
    count_upper = 0
    count_lower = 0
    for letter in word:
        if letter.isupper() :
            count_upper =count_upper + 1
        elif letter.islower():
            count_lower = count_lower + 1
    return count_upper, count_lower


print(checking_word("PPython"))
print(checking_word("java"))









