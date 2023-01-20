#This program to check whether entered number is prime or not
num=int(input("Enter a number :"))
j=0
for i in range(2,num):
    if (num%i)==0:
        j=1
        break
if j==1:
    print("Entered Number is not prime")
else:
    print("Entered Number is prime")
