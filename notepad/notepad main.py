import os.path
import time

print(os.getcwd())
file = open("testing.txt", "a")

def main():
    j = input("what would you like to do? ")
    if j == "read":
        read()
    if j == "write":
        write()
    if j == "quit" or "exit":
        print("exiting")
        exit()
    if j == "clear":
        clear()
    if j == "help":
        print("these are the options: \n read \n write \n quit / exit \n help \n clear")
        main()

def write():
    tekst = input("what would you like to type: ")
    nextline = input("moet dit op de volgende lijn? yes/no: ")

    if nextline == "yes":
        printit = file.write("\n")
        printit = file.write(tekst)
        strprintit = str(printit)
        exec(strprintit)
        file.flush()
        read()
        con()

    if nextline == "no":
        printit = file.write(tekst)
        strprintit = str(printit)
        exec(strprintit)
        file.flush()
        read()
        con()

def con():
    cont = input("write another line? yes/no: ")
    if cont == "yes":
        write()
    if cont == "no":
        main()
    else:
        print("please say yes or no ")
        con()

def read():
    f = open("testing.txt", "r")
    i = 1
    if i == 1:
        print(f.read())
        main()

def clear():
    print("clearing file")
    #als de file niet eerder is ge-opend sluit het Programma
    #if file oppend loop is nodig
    file.truncate(0)
    print("cleared file")
    main()

x = 1
if x == 1:
    x = x - 1
    main()
else:
    con()
    x = x + 1
