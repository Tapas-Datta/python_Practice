score_list =[]
i= int(input("Enter how many number you want to add  :"))
for number in range(i):
    num = int(input("Enter a number: ") )
    score_list.append(num)
print("The score list is",score_list)
print("The length of score list is",(len(score_list)))
for number in score_list:
    highest_score = score_list[0]
    lowest_score = score_list[0]
    total_marks = 0
    passed_count = 0
    failed_count = 0
    total_marks += number
    average = total_marks / len(score_list)
    if number >= 18:
        passed_count += 1
        print("total passed:",passed_count)
    if number < 18:
        failed_count += 1
        print("total failed:",failed_count)
    if number > highest_score:
        highest_score = number
        print("highest score:",highest_score)
    if number < lowest_score:
        lowest_score = number
        print("lowest score:",lowest_score)




