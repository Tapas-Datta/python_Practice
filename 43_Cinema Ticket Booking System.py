user_name= input("Enter your name: ")
print("Name:",user_name)
def movie(name  ,quantity):
    name = name.lower()
    if name not in  ["avatar","batman","spider man"]:
        return "Invalid movie choice"
    elif quantity <= 0:
        return "Invalid quantity"
    if name =="avatar":
        price = quantity* 12
    elif name =="batman":
        price = quantity * 10
    elif name =="spider man":
        price = quantity* 8
    if quantity >= 5:
        discount = price *0.10
        final_price = price - discount
    elif quantity >= 1:
        discount = 0
        final_price = price - discount
    return price,discount,final_price
while True:
    movie_name= input("Enter your movie name: ")
    ticket_quantity= int(input("Enter your quantity: "))
    result = movie(movie_name,ticket_quantity)
    if result == "Invalid movie choice" or result == "Invalid quantity":
        print(result)
    else:
        price,discount,final_price = result
        print("your initial price is ",price)
        print("your initial discount is ",discount)
        print("your final price is ",final_price)
        user = input("do you want to do another transction: ")
        if user.lower() != "yes":
            break

