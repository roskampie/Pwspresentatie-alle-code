'''
def main():
    x = input("put your equation here: ")
    if x == "a":
        print("kaas")
        exit()
    else:
        print(eval(x))
        print("kaasjes")
        main()
main()
'''

x = input("put your equation here: ")
if x == 'a':
    print("kaas")
    exit()