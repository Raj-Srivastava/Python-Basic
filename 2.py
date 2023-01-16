#This Program to find the largest of three given numbers
n1=int(input("Enter First Integer : "))
n2=int(input("Enter Second Integer : "))
n3=int(input("Enter Third Integer : "))
largest=n1
if n2>largest:
    largest=n2
if n3>largest:
    largest=n3
print("Largest Number is ",largest)