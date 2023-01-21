#This program to print factorial of entered number using function
def fact(num):
    j=1
    for i in range(1,num+1):
        j=j*i
    print(j)

num=int(input("Enter a Number:"))
fact(num)