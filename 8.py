#this program to add all digit of one number
num=int(input("Enter a Number : "))
anum=0
while(num>0):
    rem=num%10
    anum=anum+rem
    num=num//10
print("After adding all digit are : ",anum)
