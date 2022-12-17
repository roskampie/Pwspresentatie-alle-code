import random
'''
def main():
    x = input("make your choice: ")
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
        print("sciccor")
        if x == "rock":
            print("you win!\n")
        elif x == "paper":
            print("you lose\n")
        elif x == "sciccor":
            print("draw\n")
        main()
main()
'''
#old code
def main():
    global x
    x = input("make your choice: ")
    picker()
    winner()

def picker():
    global y
    number = random.randrange(1, 4)
    #asing a random choice to your opponent
    y = float(number)
#1 is sciccors
#2 is rock
#3 is paper
def winner():
    global x, y
    if x == "rock" and y == 1 or x == "paper" and y == 2 or x == "sciccors" and y == 3:
        print("you win!\n")
        main()
        #if you chose sciccors
    elif x == "rock" and y == 2 or x == "paper" and y == 3 or x == "sciccors" and y == 1:
        print("its a draw\n")
        main()
        #if you chose rock
    elif x == "rock" and y == 3 or x == "paper" and y == 1 or x == "sciccors" and y == 2:
        print("you lose\n")
        main()
        #if you chose paper
    elif x == "kaas":
        print("YOU WINN!\n")
        main()
        #fun little exeption
main()
#start the entire loop