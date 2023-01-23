#This program to write those line which have  p character
def change(fread):
    fwrite=str(input("Enter Write File name with path"))
    opfile=open(fread,"r")
    opfil=open(fwrite,"w")
    s=opfile.readlines()
    for i in s:
        if 'p' in i:
            opfil.write(i)
    opfile.close()
    opfil.close()
fread=str(input("Enter Read File Name with Path:"))
change(fread)