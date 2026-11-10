

def electricity_billing(unit):
    if unit <= 0:
        return "invalid unit"
    elif 0 < unit <= 100:
        billing = unit * 0.10
    elif 100 < unit <= 200:
        billing = (100 * 0.10) + ((unit -100) * 0.15)
    elif 200 < unit <= 300:
        billing =  (100 * 0.10) + (100* 0.15) + ((unit -200) * 0.20)
    elif unit > 300:
        billing = (100 * 0.10) + (100* 0.15) + ((100 * 0.20) +(unit -300) * 0.25)
    if  billing > 50:
        discount = billing * 0.05
        final_bill = billing - discount
    else:
        discount =0
        final_bill = billing
    return billing, discount, final_bill
while True:
    user = input("Enter your name: ")
    unit_1 = int(input("Enter your unit: "))
    electricity_billing_2= electricity_billing(unit_1)
    if electricity_billing_2 == "invalid unit":
        print('Error input')
    else:
        billing, discount, final_bill =electricity_billing_2
        print("Customer name: ", user)
        print("Billing:", billing)
        print("Discount:", discount)
        print("Final bill:", final_bill)
    choice = input("Do you want another  (yes/no): ")
    if choice.lower() == "no":
        break

