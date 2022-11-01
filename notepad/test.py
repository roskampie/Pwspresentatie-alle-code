import os.path
import time

print(os.getcwd())
f = open("testing.txt", "a")
tekst = input("what would you like to type: ")
nextline = input("moet dit op de volgende lijn? yes/no: ")
print(type(tekst))

if nextline == "yes":
    printit = f.write("\n")
    printit = f.write(tekst)
    strprintit = str(printit)
    exec(strprintit)
    f.flush()

if nextline == "no":
    print(type(tekst))
    printit = f.write(tekst)
    strprintit = str(printit)
    print(type(strprintit))
    exec(strprintit)
    f.flush()


file = open("testing.txt", "r")
i = 1
while i == 1:
    print(file.read())
    time.sleep(5)


i = 0
f.close()