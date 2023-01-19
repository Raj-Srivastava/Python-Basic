#this program to print fibonacci series
terms=int(input("How many terms user want : "))
n1=0
n2=1
i=0
if(terms==0):
    print("Error input",n1)
elif(terms==1):
    print("Error input",n2)
else:
    print("The fibonacci series is :")
    while(terms>i):
        print(n1)
        c=n1+n2
        n1=n2
        n2=c
        i+=1