full_marks = 500
student= input("Enter your name: ")
first_subject = int(input("Enter your 1st subject marks: "))
second_subject = int(input("Enter your 2nd subject: "))
third_subject = int(input("Enter your 3rd subject marks: "))
fourth_subject = int(input("Enter your 4th subject marks: "))
fifth_subject = int(input("Enter your 5th subject marks: "))
total_marks = first_subject + second_subject + third_subject + fourth_subject + fifth_subject
print("Total Marks",total_marks)
avg_marks = total_marks / 5
print("avg_marks",avg_marks)
percentage_marks =  (total_marks / full_marks) * 100
print("percentage_marks",percentage_marks)
if 90 <= percentage_marks <= 100:
    print("You got A+")
elif 80 <= percentage_marks < 90:
    print("You got A")
elif 70 <= percentage_marks < 80:
    print("You got B")
elif 60 <= percentage_marks < 70:
    print("You got C")
elif 50 <= percentage_marks < 60:
    print("You got D")
else:
    print("You are failed")