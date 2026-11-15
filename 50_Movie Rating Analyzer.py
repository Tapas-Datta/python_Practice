

name_1 = input("Enter your name: ")
movie_name = []
movie_rating = []
total_movie = 0
number_of_movies_ratings =int(input("Enter the number of movies rating you want: "))
for i in range(number_of_movies_ratings):
    name = input("Enter your movie name: ")
    total_movie += 1
    movie_name.append(name)

    rating = int(input("Enter your movie ratings from 1 to 10: "))
    movie_rating.append(rating)
def analyze_movies(movie_rating):
    if not movie_rating:
        return None
    total = 0
    count = 0
    count_1 = 0
    count_2 = 0
    highest = movie_rating[0]
    lowest = movie_rating[0]
    for movie in movie_rating:
        total += movie
        if movie >highest:
            highest = movie
        if movie <lowest:
            lowest = movie
        if movie <5:
            count += 1
        if movie >= 8:
            count_1 +=1
        if movie == 10:
            count_2 += 1
    average = total / len(movie_rating)
    if average  >= 8:
        overall_performance ="Excellent"
    elif average >= 6:
        overall_performance = "Good"
    elif average >= 4:
        overall_performance = "Average"
    else:
        overall_performance = "Poor"
    return average, highest , lowest , count, count_1, count_2  ,overall_performance
result = analyze_movies(movie_rating)
if result is None:
    print("No text entered.")
else:
    average, highest, lowest, count, count_1, count_2,overall_performance = result
    print("======================================")
    print("Name",name_1)
    print("Total movie ratings",number_of_movies_ratings)
    print("Average Rating:", average)
    print("Highest Rating:", highest)
    print("Lowest Rating:", lowest)
    print("Count Rating less than 5 rating:", count)
    print("Count 1 Rating more than 8:", count_1)
    print("Count 2 Rating exactly 10:", count_2)
    print("Overall Performance:", overall_performance)






