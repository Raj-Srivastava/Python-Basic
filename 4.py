#This Program is menu driven to perform arithematic operation
num1=int(input("Enter First Number : "))
num2=int(input("Enter Second Number : "))
print("1.Add")
print("2.Subtract")
print("3.Division")
print("4.Multiplication")
choice=int(input("Enter Your choice : "))
if choice==1:
    add=num1+num2
    print("Addition = ",add)
elif choice==2:
    sub=num1-num2
    print("Subtraction = ",sub)
elif choice==3:
    div=num1/num2
    print("Division = ",div)
elif choice==4:
    mult=num1*num2
    print("Multiplication = ",mult)
else:
    print("Wrong Input")