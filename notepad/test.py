import os.path
import time

print(os.getcwd())
file = open("testing.txt", "a")
tekst = input("what would you like to type: ")
nextline = input("moet dit op de volgende lijn? yes/no: ")
print(type(tekst))

if nextline == "yes":
    printit = file.write("\n")
    printit = file.write(tekst)
    strprintit = str(printit)
    exec(strprintit)

if nextline == "no":
    print(type(tekst))
    printit = file.write(tekst)
    strprintit = str(printit)
    print(type(strprintit))
    exec(strprintit)


f = open("testing.txt", "r")
i = 1
while i == 1:
    print(f.read())
    time.sleep(5)


i = 0
file.close()