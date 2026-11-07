def employee_salary(basic_salary, experience, performance_bonus):
    if basic_salary <= 0:
        return "invalid salary"
    if experience < 0:
        return "invalid experience"
    if experience < 2:
        employee_bonus_salary = 0
    elif 2 <= experience <= 5:
        employee_bonus_salary = basic_salary * 0.05
    elif experience > 5:
        employee_bonus_salary = basic_salary * 0.10
    else:
        return "invalid experience"
    if performance_bonus == "yes":
        employee_performance_bonus_salary = basic_salary * 0.15
    elif performance_bonus == "no":
        employee_performance_bonus_salary = basic_salary * 0
    else:
        return "invalid choice"
    employee_final_salary = basic_salary + employee_bonus_salary + employee_performance_bonus_salary
    if employee_final_salary > 50000:
        employee_tax = employee_final_salary * 0.10
        employee_after_tax = employee_final_salary - employee_tax
    else:
        employee_tax = employee_final_salary * 0.05
        employee_after_tax = employee_final_salary - employee_tax
    return employee_bonus_salary, employee_performance_bonus_salary, employee_final_salary, employee_tax, employee_after_tax