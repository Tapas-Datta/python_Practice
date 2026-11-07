
correct_number = 40
count = 0
while count < 5:
    number = int(input("enter the guessing number from 1 to 100 :"))
    if number == correct_number:
        print("you guessed correctly")
        break
    elif number > correct_number:
        count = count + 1
        print("you guessed too high")
    elif number < correct_number:
        count = count + 1
        print("you guessed too low")
if count == 5:
    print("you tried max")




