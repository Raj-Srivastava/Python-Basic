#This program to calculate total number of vowels in text file
def calc(fname):
    opfile=open(fname,"r")
    total=0
    vowels=['a','e','i','o','u','A','E','I','O','U']
    for val in opfile.readline():
        if val in vowels:
            total=total+1
    opfile.close()
    if total>=1:
        print("There are" + str(total) + "vowels in file")
    else:
        print("There are no vowels in file")
fname=str(input("Enter File Name with Path:"))
calc(fname)