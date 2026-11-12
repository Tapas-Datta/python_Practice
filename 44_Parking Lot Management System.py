name = input("Enter your name: ")
def vehicle_type(veh_type,hour):
    veh_type = veh_type.lower()
    if veh_type not in ["bike","car","truck"]:
        return "Invalid Vehicle Type"
    elif hour <=0 :
        return "Invalid Hour"

    if veh_type.lower() == "bike":
        cost = 2 * hour
    elif veh_type.lower() == "car":
        cost = 5 * hour
    elif veh_type.lower() == "truck":
        cost = 8 * hour

    if hour > 10:
        extra = 5
        discount = cost * 0.10

    elif hour > 5:
        extra = 0
        discount = cost * 0.10

    else:
        extra = 0
        discount = 0
    final_bill = cost - discount + extra
    return cost,discount,extra,final_bill
while True:
    veh_types = input("Enter your Vehicle Type: ")
    hours = int(input("Enter your Hours: "))
    result = vehicle_type(veh_types,hours)
    if result == "Invalid Vehicle Type" or result == "Invalid Hour":
        print(result)
    else:
        cost,discount,extra,final_bill = result
        print("name",name)
        print("Vehicle Type:", veh_types)
        print("Parking Hours:", hours)
        print("original fees:",cost)
        print("Discount:",discount)
        print("Extra :",extra)
        print("Final fees:",final_bill)
    user = input("Do want to continue again")
    if user.lower() != "yes":
        break

