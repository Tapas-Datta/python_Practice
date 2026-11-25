reviewer_list = []
rating_list = []
name_list = []
quantity = int(input("Enter how many movie rating you want to input: "))
for i in range(quantity):
    name = input("Enter the movie name: ")
    name_list.append(name)
    reviewer = int(input("Enter the number of reviewers: "))
    reviewer_list.append(reviewer)
    rating = float(input("Enter the rating of the movie: "))
    rating_list.append(rating)
    if 8 <= rating <= 10:
        print("Excellent")
    elif 6 <= rating < 8:
        print("Good")
    elif 4 <= rating < 6:
        print("Average")
    else:
        print("poor")

def movie_rating(rating_list,reviewer_list,name_list):
    excellent =  0
    poor = 0
    highest_review_score = []
    highest = rating_list.index(max(rating_list))
    lowest = rating_list.index(min(rating_list))
    total_review = sum(reviewer_list)
    average_rating = sum(rating_list)/len(rating_list)
    for j in rating_list:
        if j >= 8:
            excellent += 1
        elif j < 4:
            poor += 1
    for k in range(len(reviewer_list)):
        highest_review_score.append (rating_list[k] * reviewer_list[k])
    highest_2 = highest_review_score.index(max(highest_review_score))
    return average_rating, highest, lowest, excellent, poor, total_review, highest_2, highest_review_score

final = movie_rating(rating_list,reviewer_list,name_list)
average_rating,highest,lowest,excellent,poor,total_review,highest_2,highest_review_score = final
print("Total Movie",quantity)
print("average rating: ",average_rating)
print("highest rating: ",name_list[highest],max(rating_list))
print("lowest rating: ",name_list[lowest],min(rating_list))
print("excellent: ",excellent)
print("poor: ",poor)
print("Total reviews: ",total_review)
print("highest review_score: ",name_list[highest_2],highest_review_score[highest_2])


    

