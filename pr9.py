#This Program to count number of words in a text file
def count(fname):
    opfile=open(fname,"r")
    data = opfile.read()
    words = data.split()
    print('Number of words in text file :', len(words))

fname=str(input("Enter file name with path "))
count(fname)