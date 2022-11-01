import os.path
import time

print(os.getcwd())
file = open("testing.txt", "a")

def main():
    j = input("read or write?")
    if j == "read":
        f = open("testing.txt", "r")
        i = 1
        while i == 1:
            print(f.read())
    if j == "write":
        write()

def write():
    tekst = input("what would you like to type: ")
    nextline = input("moet dit op de volgende lijn? yes/no: ")
    print(type(tekst))

    if nextline == "yes":
        printit = file.write("\n")
        printit = file.write(tekst)
        strprintit = str(printit)
        exec(strprintit)
        file.flush()

    if nextline == "no":
        print(type(tekst))
        printit = file.write(tekst)
        strprintit = str(printit)
        print(type(strprintit))
        exec(strprintit)
        file.flush()

def con():
    cont = input("write another line? yes/no: ")
    if cont == "yes":
        main()
    if cont == "no":
        file.close()
        exit()
    else:
        print("please say yes or no ")
x = 1
if x == 1:
    x = x - 1
    write()
else:
    con()
