amount_list = []
days = int(input("Enter the number of days sales amount: "))
for i in range (days):
    amount = int(input("Enter the sales amount: "))
    amount_list.append(amount)
    if amount >= 500:
        print("Wow!! High sell",)
    elif 300 <= amount < 500:
        print("Good Sales" )
    elif 100 <= amount < 300:
        print("Average Sales")
    elif 0< amount < 100:
        print("Low sales")
def sales_list(amount_list):
    total_sales = 0
    count = 0
    count_1 = 0
    highest = amount_list[0]
    lowest = amount_list[0]
    for sale in amount_list:
        total_sales += sale
        if sale > highest:
            highest = sale
        if sale < lowest:
            lowest = sale
        if sale >= 500:
            count += 1
        if sale < 100:
            count_1 +=1
    days_with_highest = amount_list.index(max(amount_list))
    days_with_lowest = amount_list.index(min(amount_list))
    average = total_sales / len(amount_list)
    return total_sales,average, count, count_1, highest, lowest,days_with_highest,days_with_lowest
final = sales_list(amount_list)
total_sales,average, count, count_1, highest, lowest,days_with_highest,days_with_lowest = final
print("total days",days)
print("total sales: ",total_sales)
print("average sales: ",average)
print("High Sales days: ",count)
print("sales less than 100: ",count_1)
print("highest sales: ",days_with_highest + 1,highest)
print("lowest sale: ",days_with_lowest + 1, lowest)


        