#This program to check whether entered string is palindrome or not using function
def chk(str):
    if(str==str[::-1]):
        print("Entered String is palindrome")
    else:
        print("Entered string is not palindrome")
str=input("Enter a String")
chk(str)