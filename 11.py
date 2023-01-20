#This program to print factorial of a given or entered numbers
num=int(input("Enter a number :"))
fac=1
for i in range(1,num+1):
    fac=fac*i
print("Factorial of entered number is :",fac)
