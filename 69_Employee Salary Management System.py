user = int(input("enter the name how many employees name you want to have: "))
salary_list = []
def salary(basic_salary, working_hours):
    if working_hours > 40:
        total_salary = basic_salary + (basic_salary * 0.10)
    else:
        total_salary = basic_salary

    if basic_salary > 2000:
        tax = basic_salary * 0.05
    else:
        tax = 0
    final_salary = total_salary - tax
    return final_salary
for i in range(user):
    name = input("enter your name: ")
    basic_salary = int(input("enter your basic salary: "))
    working_hours = int(input("enter your working hours: "))
    final_salary = salary(basic_salary, working_hours)
    salary_list.append(final_salary)
    print("----------------------")
    print("Name:", name)
    print("Basic Salary:", basic_salary)
    print("Working Hours:", working_hours)
    print("Final Salary:", final_salary)
    print("----------------------")