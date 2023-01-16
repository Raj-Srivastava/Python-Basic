#This Program for calculating simple interest
p_amount=int(input("Enter Principal amount : "))
time=int(input("Enter Time in years : "))
if time>10:
    print("Calculating SI with interest rate 8%")
    si=p_amount*time*8/100
    total_amount=si+p_amount
else:
    print("Calculating SI with interest rate 12%")
    si=p_amount*time*12/100
    total_amount=si+p_amount
print("Simple Interest = ",si)
print("Total Amount = ",total_amount)