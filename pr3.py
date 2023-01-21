#This program to check whether entered value is digit, alphabet or anything else using function
def chk(char):
    if char[0].isalpha():
        print("Entered character is alphabet")
    elif char[0].isdigit():
        print("Entered character is a digit")
    else:
        print("Entered character is a special character")

char=input("Enter a character")
chk(char)