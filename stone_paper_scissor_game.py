import random

def play_game():
    a = int(input("Enter your move (0: stone, 1: paper, 2: scissors)"))
    b = random.randint(0, 2)

    if a == b:
        print("Match Draw as Opponent also choosed the same Move As Yours")
    elif a == 0 and b == 1:
        print("Opponent Chooses Paper You choosed stone so you lost")
    elif a == 1 and b == 0:
        print("Opponent Choosed Stone You Choosed Paper so you won")
    elif a == 0 and b == 2:
        print("Opponent Choosed scissor and you Choosed stone so you won")
    elif a == 2 and b == 0:
        print("Opponent choosed stone and you choosed scissor so you lost")
    elif a == 1 and b == 2:
        print("Opponent Choosed Scissor and you choosed paper so you lost")
    elif a == 2 and b == 1:
        print("Opponent Choosed Paper and You choosed scissor so you won")
    else:
        print("Not A Valid Move")

while True:
    print("\033 Welcome To Stone Paper Scissor Game! \033")
    option = int(input("*Press:- \n [1] Play. \n [2] Exit. \n "))
  
    if option == 1:
        play_game()
    elif option == 2:
        print("Thanks for playing,see you soon,Goodbye!")
        break
    else:
        print("Invalid option. Please enter 1 to play or 2 to exit.")