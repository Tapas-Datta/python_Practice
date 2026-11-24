mark_bucket = []
name_bucket = []
average_bucket = []
total_bucket = []
count_gade_A = 0
student = int(input("enter how many students details do you want to see: "))
def marks_calculator(math_marks, english_marks, computer_marks):

    total_marks = math_marks + english_marks + computer_marks
    average_marks = total_marks / 3

    if 80 <= average_marks <= 100:
        grade = "A"
    elif 70 <= average_marks < 80:
        grade = "B"
    elif 60 <= average_marks < 70:
        grade = "C"
    elif 50 <= average_marks < 60:
        grade = "D"
    else:
        grade = "F"

    return total_marks, average_marks, grade


for i in range(student):

    student_name = input("enter your name: ")
    name_bucket.append(student_name)

    math_marks = int(input("enter your math marks: "))
    english_marks = int(input("enter your english marks: "))
    computer_marks = int(input("enter your computer marks: "))

    final = marks_calculator(math_marks, english_marks, computer_marks)

    total_marks, average_marks, grade = final

    total_bucket.append(total_marks)
    average_bucket.append(average_marks)

    if grade == "A":
        count_gade_A += 1
    print("================================================")
    print("Name:", student_name)
    print("Total marks:", total_marks)
    print("Average marks:", average_marks)
    print("Grade:", grade)
def class_summary(average_bucket, name_bucket):
    total = 0
    pass_count = 0
    fail_count = 0

    highest = average_bucket[0]
    lowest = average_bucket[0]

    highest_name = name_bucket[0]
    lowest_name = name_bucket[0]

    for i in range(len(average_bucket)):

        marks = average_bucket[i]
        total += marks

        if marks > highest:
            highest = marks
            highest_name = name_bucket[i]

        if marks < lowest:
            lowest = marks
            lowest_name = name_bucket[i]

        if marks >= 50:
            pass_count += 1
        else:
            fail_count += 1

    class_average = total / len(average_bucket)

    return highest_name, lowest_name, class_average, highest, lowest, pass_count, fail_count


final_1 = class_summary(average_bucket, name_bucket)

highest_name, lowest_name, class_average, highest, lowest, pass_count, fail_count = final_1

print("================================================")
print("Class Average:", class_average)
print("Highest Student:", highest_name, highest)
print("Lowest Student:", lowest_name, lowest)
print("Pass count:", pass_count)
print("Fail count:", fail_count)
print("Grade A:", count_gade_A)