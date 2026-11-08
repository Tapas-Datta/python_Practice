
def employee(working_days_1, days_1, salary_1):
    while True:
        if working_days_1 == 0:
            return "invalid working days"
        elif days_1== 0:
            return "invalid days"
        attendance_1 = (working_days_1 / days_1) * 100
        full_salary_1 = salary_1
        if attendance_1 >= 90:
            full_salary_1 = salary_1
        elif 75 <= attendance_1 < 90:
            cut = salary_1 * 0.10
            full_salary_1 = salary_1 -cut
        elif attendance_1 <75 :
            cut = salary_1 * 0.20
            full_salary_1 = salary_1 -cut
        return attendance_1,full_salary_1

name= input("Enter your name: ")
days = int(input("Enter days of that month : "))
working_days = int(input("Enter your working days: "))
salary = int(input("Enter your salary: "))
result=employee(working_days,days,salary)
if result == "invalid working days" or result == "invalid days":
    print(result)
else:
    attendance, full_salary = result
    print(f"attendance: {attendance}%")
    print("full_salary:", full_salary)