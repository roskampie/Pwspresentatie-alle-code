def main():
    x = input("put your equation here: ")
    if x == "exit":
        print("exiting")
        exit()
    else:
        print(eval(x))
        print("kaasjes")
        main()
main()
