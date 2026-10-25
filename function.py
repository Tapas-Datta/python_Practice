def find_max(number_1,number_2):
    if number_1 > number_2:
        return "a"
    else:
        return "b"
highest=find_max(4,5)
print(highest)


def is_leap_year(year):
    if year % 4==0:
        return "leap year"
    else:
        return "not leap year"
leap_year = is_leap_year(int(input("Enter the year you want to check")))
# print(leap_year)


def count(word):
    return len(word)
user = count(input("Enter  what you want to know the len : "))
print(user)


def is_item_in_list(item,my_list):
    if item in my_list:
        return True
    else:
        return False
my_list = ["apple", "banana", "cherry"]
item_find = is_item_in_list(input("Enter the stuff you are looking for"), my_list)
print(item_find)

def double_first_item(my_list):
    double = my_list[0]*2
    return double
my_list = [10, 2, 3, 4, 5]
x = double_first_item(my_list)
print(x)


