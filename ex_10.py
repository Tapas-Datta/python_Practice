# def checking_positive(value):
#     total =  0
#     for number in value:
#         if number > 0:
#             total += 1
#     return total
# def checking_negative(value):
#     total_1 = 0
#     for number_1 in value :
#         if number_1 < 0:
#             total_1 += 1
#     return total_1
#
# numbers = [4, -2, 0, 7, -1, 5]
# print(checking_positive(numbers))
# print(checking_negative(numbers))
#
# def checking_number(value):
#     total =  0
#     total_1 = 0
#     total_2 = 0
#     for number in value:
#         if number > 0:
#             total += 1
#         elif number < 0:
#             total_1 += 1
#         elif number ==0:
#             total_2 += 1
#     return total,total_1,total_2
# user = numbers = [4, -2, 0,0, 7, -1, 5]
# print(checking_number(numbers))

#
# def checking_number(value):
#     maxi = value[0]
#     mini = value[0]
#     total_sum = 0
#     count = 0
#     for number in value:
#         total_sum += number
#         count += 1
#         avg_value = total_sum / count
#         if number > maxi:
#             maxi = number
#         elif number < mini:
#             mini = number
#     return maxi, mini, avg_value
# values_1 = [18, 12, 25, 7, 20]
# print(checking_number(values_1))

#
# def count_vowels(word):
#     count = 0
#     for letter in word :
#         if letter in "aeiou":
#             count += 1
#     return count
# enter_text = "programming"
# print(count_vowels(enter_text))
#
# def find_first(number):
#     for number_1 in number:
#         return number_1 []

# def reverse_list(number):
#     return number [::-1]
# list_1 =[40, 30, 20, 10]
# print(reverse_list(list_1))
#
# def is_palindrome(text):
#     if text == text[::-1]:
#         return True,text
#     else:
#         return False,text
# user_1 = input("Enter a name: ")
# print(is_palindrome(user_1))



def average(value):
    total = 0
    count = 0
    for number in value:
        total +=  number
        count = count + 1
    final = total/count
    return final

def extremes(value):
    mini_mum = value[0]
    maxi_mum = value[0]
    for number in value:
        if number < mini_mum:
            mini_mum = number
        if number > maxi_mum:
            maxi_mum = number
    return mini_mum, maxi_mum

def count_above(value, threshold):
    count = 0
    for number in value:
        if number > threshold:
            count = count + 1
    return count

n = int(input("Number of measurements: "))
while n <= 0:
    print("Please enter a positive integer.")
    n = int(input("Number of measurements: "))

measurements = []
for i in range(n):
    temp = float(input(f"Measurement {i + 1}: "))
    measurements.append(temp)

avg_result = average(measurements)
min_result, max_result = extremes(measurements)
above_avg_result = count_above(measurements, avg_result)

print(f"Measurements: {measurements}")
print(f"Average: {avg_result}")
print(f"Minimum: {min_result}")
print(f"Maximum: {max_result}")
print(f"Above average: {above_avg_result}")



