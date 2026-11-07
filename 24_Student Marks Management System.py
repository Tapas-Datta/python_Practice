student_name_1 = input("Enter Student Name")
student_marks_1 = int(input('Enter Student Marks: '))
student_name_2 = input("Enter Student Name")
student_marks_2 = int(input('Enter Student Marks: '))
student_name_3 = input("Enter Student Name")
student_marks_3 = int(input('Enter Student Marks: '))
student_name_4 = input('Enter Student Name')
student_marks_4 = int(input('Enter Student Marks: '))
student_name_5 = input('Enter Student Name')
student_marks_5 = int(input('Enter Student Marks: '))

all_student_name = [student_name_1, student_name_2, student_name_3, student_name_4, student_name_5]
print("all  student name", all_student_name)
all_student_marks= [student_marks_1, student_marks_2, student_marks_3, student_marks_4, student_marks_5]
print("all student marks ",all_student_marks)

total_marks = sum(all_student_marks)
print("total marks",total_marks)
average_marks =sum(all_student_marks)/len(all_student_marks)
print("average marks ",average_marks)

lowest_marks = min(all_student_marks)
print("low marks is",lowest_marks)
highest_marks = max(all_student_marks)
print("highest marks ",highest_marks)

for all_marks in all_student_marks:
    if all_marks > 50:
        print("pass marks",all_marks)
    else:
        print("fail marks is ",all_marks)