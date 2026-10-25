
n = int(input("Enter positive integer: "))
factorial = 1
for i in range(1, n + 1):
  factorial *= i
print(f"{n}! factorial of your number is {factorial}")


def sum_evens(numbers_list):
  total_evens = 0
  for number in numbers_list:
    if number % 2 == 0:
      total_evens += number
  return total_evens
evens_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
final_evens_list = sum_evens(evens_list)
print(final_evens_list)

def check_max(numbers):
  largest = numbers[0]
  for max_number in numbers:
    if max_number > largest:
      largest = max_number
  return largest
my_list = [12, 45, 7, 89, 23, 5]
final_max = check_max(my_list)
print(final_max)

def avg_sum(numbers):
  total = 0
  for number in numbers:
    total += number
    avg_1 = total / len(numbers)
  return avg_1
my_list = [12, 45, 7, 89, 23, 5]
final_avg = avg_sum(my_list)
print(final_avg)


def guess_number(secret_number):
  while True:
    user_guess = int(input("Enter your guess: "))
    if user_guess == secret_number:
      print("You guessed the number")
      break
    elif user_guess < secret_number:
      print("Your guess is too low! try again: ")
    elif user_guess > secret_number:
      print("Your guess is too high! try again")
guess_number(7)


