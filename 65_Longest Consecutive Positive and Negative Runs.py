user = int(input("How many numbers would you like to add? "))
number_list = []
for i in range(user):
    number= int((input("please,enter your number serially: ")))
    number_list.append(number)
def consecutive_run(number_list):
    positive_run = []
    negative_run = []
    longest_positive_run = []
    longest_negative_run = []
    zero = 0
    for number in number_list:
        if number > 0:
            positive_run.append(number)
            negative_run = []
            if len(positive_run) > len(longest_positive_run):
                longest_positive_run = positive_run [:]

        elif number < 0:
            negative_run.append(number)
            positive_run = []
            if len(negative_run) >len(longest_negative_run):
                longest_negative_run = negative_run [:]
        else:
            zero += 1
            positive_run = []
            negative_run = []
    return longest_positive_run, longest_negative_run, zero
final = consecutive_run(number_list)
print("=======================")
longest_positive_run, longest_negative_run, zero = final
print("longest positive sequence",longest_positive_run)
print("longest positive sequence length",len(longest_positive_run))
print("longest negative sequence",longest_negative_run)
print("longest negative sequence length",len(longest_negative_run))
print("Zero",zero)








