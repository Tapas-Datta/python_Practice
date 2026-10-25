
def sum_first_two(my_list):
    sum_1_2 =my_list[0] + my_list[1]
    return sum_1_2
number =[1,2,3,4,5]
total = sum_first_two(number)
print(total)


def add_num(my_list, new_name):
    my_list.append(new_name)
    return my_list
already_there = ["Rain", "Ratul", "Rahim"]
final = add_num(already_there, "Karim")
print(final)

def remove_item(my_list, name_to_remove):
    my_list.remove(name_to_remove)
    return my_list
all_list = [1, 2, 3, 4, 5]
final= remove_item(all_list,2)
print(final)

def add_two_to_all(my_list):
    return my_list
list_1=[1,2,3,4,5]
final =add_two_to_all(len(list_1 *2 ))
print(final)

def checking(my_list):
    for i in my_list :
        if i%2 == 0:
            print("EVEN")
        else:
            print("ODD")
user = [1,2,3,4,5,6,7,8,9 ]
checking(user)

def user(positive):
    if positive >0:
        print("That's positive number")
    else:
        print("That's negative number")
number = int(input("Enter a number: "))
user(number)

def positive(my_list):
    for number in my_list:
        if number %2 == 0 :
            print("EVEN")
        else:
            print("ODD")
my_list_11 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
positive(my_list_11)


def check_grades(scores_list):
    for number in scores_list:
        if number >= 50:
            print("PASSED")
        else:
            print("FAILED")
checking=[int(input("Enter a number: "))]
check_grades(checking)

def check_grades(scores_list):
    for number in scores_list:
        if number >= 50:
            print("passed")
        else:
            print("failed")
numbers_list = [10, 20, 30, 40, 110]
check_grades(numbers_list)

def check_attendance(names_list):
    for attendance in names_list:
        if attendance == "Rahim".lower():
            print("Present")
        else:
            print("Not present")
attendace_list = [input("Enter your name: ")]
check_attendance(attendace_list)






