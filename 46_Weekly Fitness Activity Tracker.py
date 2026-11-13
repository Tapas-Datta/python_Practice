name = input("Enter your name: ")
days = int (input("Enter how many days you want to track: "))
step = []
for i in range(days):
    user_input = int(input("Enter your daily activity count"))
    step.append(user_input)
def analyze_activity(step):
    if not step:
        return None
    total = 0
    highest_steps = step[0]
    lowest_steps = step[0]
    step_count = 0
    step_count_1 = 0
    for steps in step:
        if steps > highest_steps:
            highest_steps = steps
        if steps < lowest_steps:
            lowest_steps = steps

        if steps >= 10000:
            step_count += 1
        if steps < 5000:
            step_count_1 += 1


    for daily_step in step:
        total += daily_step
    average = total / len(step)

    if average < 3000:
        level = "Very Low"
    elif average < 6000:
        level = "Low"
    elif average < 10000:
        level = "Moderate"
    else:
        level = "Excellent"

    return total,average,highest_steps, lowest_steps, step_count, step_count_1,level
result = analyze_activity(step)
if result is None:
    print("No data entered.")
else:

    total,average,highest_steps, lowest_steps, step_count, step_count_1,level = result
    print("-------------Total Weekly Fitness Activity Tracker----------------")
    print("Name:", name)
    print("Days: ", days)
    print('total step: ', total)
    print('average step: ', average)
    print('highest step: ', highest_steps)
    print('lowest step', lowest_steps)
    print('days with more 10k: ', step_count)
    print('days with ess than 5k:', step_count_1)
    print('level:', level)
    









        

