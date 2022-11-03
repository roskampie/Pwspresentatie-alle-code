def main():
    x = input("put your equation here: ")
    if x == "quit" or x == "exit":
        exit()
    else:
        print(eval(x))
        main()
main()
