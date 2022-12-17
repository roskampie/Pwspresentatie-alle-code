import random
def main():
    x = input("make your choice: ")
    if x == "quit" or x == "exit":
        exit()
    else:
        number = random.randrange(1,4)
        numberx = float(number)
        print("rock...paper...scissor...shoot")
        if numberx == 1:
            print("rock")
            if x == "rock":
                print("draw\n")
            elif x == "paper":
                print("you win!\n")
            elif x == "sciccor":
                print("you lose\n")
            main()
        elif numberx == 2:
            print("paper")
            if x == "rock":
                print("you lose\n")
            elif x == "paper":
                print("draw\n")
            elif x == "sciccor":
                print("you win!\n")
            main()
        elif numberx == 3:
            print("scissor")
            if x == "rock":
                print("you win!\n")
            elif x == "paper":
                print("you lose\n")
            elif x == "scissor":
                print("draw\n")
            main()
main()