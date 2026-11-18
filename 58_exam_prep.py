user = int(input("How many numbers do you want to add: ?"))
marks = []
total_marks = 0
passed_count = 0
failed_count = 0
for number in range(user):
    teacher = int(input("enter the marks?: "))
    if teacher < 0 or teacher > 30:
        print("Invalid mark")
        exit(0)
    else:
        marks.append(teacher)
        total_marks += teacher
average = total_marks / len(marks)
highest_marks =marks [0]
lowest_marks =marks [0]
for mark in marks:

    if mark >=18:
        passed_count += 1
    if mark < 18:
        failed_count += 1
    if mark > highest_marks:
        highest_marks = mark
    if mark < lowest_marks:
        lowest_marks = mark

print(f"here is your list of marks: {marks}")
print("the length of your number is: ", len(marks))
print("Total passed: ", passed_count)
print("Total failed: ", failed_count)
print(f"the average marks is:  {average:.2f}")
print("the highest marks is: ", highest_marks)
print("the lowest marks is:", lowest_marks)


    
