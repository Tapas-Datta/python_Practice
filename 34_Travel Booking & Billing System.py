def billing(destination,passenger):
        if destination not in ["rome", "milan", "venice", "florence"]:
            return "Invalid destination"
        elif passenger <= 0:
            return "Invalid passengers"
        if destination == "rome":
            cost = 100
        elif destination == "milan":
            cost = 150
        elif destination == "venice":
            cost = 200
        elif destination == "florence":
            cost = 120
        esti_price = passenger * cost
        if passenger < 3:
            discount = esti_price * 0
        elif passenger >=3 :
            discount = esti_price * 0.10

        final_bill = esti_price - discount
        return esti_price,discount,final_bill
username=input("Enter your name: ")
destiny = input("Enter your destination: ")
passengers = int(input("Enter your passengers: "))
result = billing(destiny, passengers)
if result == "Invalid destination" or result == "Invalid passengers":
    print(result)
else:
    esti_price,discount,final_bill = result
    print("Name: ", username)
    print("your estimated price: ", esti_price)
    print("your discount: ", discount)
    print("your final bill: ", final_bill)









