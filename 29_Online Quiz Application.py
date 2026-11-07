
count = 0
while True:
    print("Which language is mainly used for styling web pages?")
    print("1 HTML")
    print("2. Java")
    print("3. C++")
    print("4. PHP")

    question_1 = int(input("Enter your choice:"))
    if question_1 == 1:
        count += 1
        print(f"your answer is correct.you score is {count}")
    else:
        print(f"your answer is wrong.correct answer is 1. HTML. you score is {count} ")
        

    print(" What is the output of 10 % 3 in Python?")
    print(" 1. 1")
    print(" 2. 2")
    print(" 3. 3")
    print(" 4. 0")
    question_2 = int(input("Enter your choice:"))
    if question_2 == 1 :
        count += 1
        print(f"your answer is correct.you score is {count}")
    else:
        print(f"your answer is wrong.correct answer is 1.your score now {count} ")


    print("What is the result of len of (python)")
    print(" 1. 5")
    print(" 2. 7")
    print(" 3. 8")
    print(" 4. 6")
    question_3 = int(input("Enter your choice:"))
    if question_3 == 4:
        count += 1
        print(f"your answer is correct.you score is {count}")
    else:
        print(f"your answer is wrong.correct answer is D.your score now {count} ")


    print("The final score of you is ",count)
    break




