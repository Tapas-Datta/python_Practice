name_list = []
total_classes_list = []
attended_classes_list = []
mark_list = []
count=0
count_1  = 0
count_2 = 0
teacher = int(input("Enter how many students details you want to add: "))
for x in range(teacher):
    name = input("Enter your student name: ")
    name_list.append(name)
    classes = int(input("Enter the number of classes you want to add: "))
    total_classes_list.append(classes)
    attended = int(input("Enter the classes you attended: "))
    attended_classes_list.append(attended)
    mark = int(input("Enter the mark of your exam: "))
    mark_list.append(mark)
    attendance_percentage = (attended / classes)  * 100
    print("Attendance percentage: ", attendance_percentage)
    if attendance_percentage >= 75:
        print("Eligible")
        count += 1
    else:
        print("Not Eligible")

    if mark >= 50:
        print("Pass")
        count_1  += 1
    else:
        print("Fail")

    if mark >= 50 and attendance_percentage >= 75:
        count_2 += 1
total_marks = 0
for k in mark_list:
    total_marks += k
average_mark = total_marks / len(mark_list)

highest_mark = max(mark_list)
position= mark_list.index(highest_mark)
name = name_list[position]
lowest_mark = min(mark_list)
position_1 = mark_list.index(lowest_mark)
name_1 = name_list[position_1]

print("Total Student:",teacher)
print("Average Mark:",average_mark)
print("Highest Mark:",highest_mark,name)
print("Lowest Mark:",lowest_mark, name_1)
print("Eligible students:",count)
print("Pass students:",count_1)
print("Eligible and pass",count_2)
