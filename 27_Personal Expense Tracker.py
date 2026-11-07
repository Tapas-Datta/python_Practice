

first_day= int(input("enter the first day_expense:"))
second_day= int(input("enter the second day_expense:"))
third_day= int(input("enter the third day_expense:"))
fourth_day= int(input("enter the fourth day_expense:"))
fifth_day= int(input("enter the fifth day_expense:"))
sixth_day= int(input("enter the sixth day_expense:"))
seventh_day= int(input("enter the seventh day_expense:"))
total_expense_list =[first_day,second_day,third_day,fourth_day,fifth_day,sixth_day,seventh_day]
print("total expense list is",total_expense_list)
total_expense = sum(total_expense_list)
print("total expense is",total_expense)
average_expense = total_expense / len(total_expense_list)
print("average expense is ",average_expense)
max_expense = max(total_expense_list)
print("max_expense is",max_expense)
min_expense = min(total_expense_list)
print("min_expense is",min_expense)
count=0
for expense in total_expense_list:
    if expense > 100:
        count += 1
print("Days with expenses above 100:",count)
if total_expense > 500:
    print("total expense is exceed 500")





