sales_list= []
for i in range (1,8,1):
    user = int(input("Enter your sales list one by one: "))
    sales_list.append(user)
def sales_analysis (sales_list):
    highest_sales = sales_list[0]
    lowest_sales = sales_list[0]
    total_sales = 0
    under_100_sales = 0
    for sale in sales_list:
        total_sales += sale
        if sale > highest_sales:
            highest_sales = sale
        if sale < lowest_sales:
            lowest_sales = sale
        if sale < 100:
            under_100_sales +=1
    average_sales = total_sales / 7
    count = 0
    count_1 = 0
    for sale_1 in sales_list:
        if sale_1 > average_sales:
            count += 1
        if sale_1 < average_sales:
            count_1 += 1
    return highest_sales,lowest_sales,total_sales,under_100_sales, count, count_1, average_sales

def consecutive_analysis(sales_list):
    run_list = [sales_list[0]]
    longest_increase = [sales_list[0]]
    length = 1
    highest_length = 1
    run_list_1 = [sales_list[0]]
    longest_decrease = [sales_list[0]]
    length_1 = 1
    highest_length_1 = 1
    for j in range(len(sales_list) - 1):
        if sales_list[j] < sales_list[j+1]:
            run_list.append(sales_list[j+1])
            length += 1
        else:
            run_list = [sales_list[j+1]]
            length = 1
        if length > highest_length:
            highest_length = length
            longest_increase = run_list.copy()
        if sales_list[j] > sales_list[j+1]:
            run_list_1.append(sales_list[j+1])
            length_1 += 1
        else:
            run_list_1 = [sales_list[j+1]]
            length_1 = 1
        if length_1 > highest_length_1:
            highest_length_1 = length_1
            longest_decrease = run_list_1.copy()

    return longest_increase, highest_length, longest_decrease, highest_length_1


final = sales_analysis(sales_list)
highest_sales,lowest_sales,total_sales,under_100_sales, count, count_1 , average_sales  = final
final_1 = consecutive_analysis(sales_list)
longest_increase, highest_length, longest_decrease, highest_length_1= final_1
print("=      ==================         =")
print("Highest sales: ",highest_sales)
print("Lowest sales: ",lowest_sales)
print("Total sales: ",total_sales)
print("Under 100 sales: ",under_100_sales)
print("sales more than average: ",count)
print("sales less than average: ",count_1)
print(f"Average sales: {average_sales:.2f}")
print("===================================")
print("increase run list: ",longest_increase)
print("decrease run list: ",longest_decrease)
print("Highest run list: ",highest_length)
print("lowest run list", highest_length_1)




