import random

print("Let's start the game")
a = ["scissor", "rock", "paper"]

user = input("Your choice: ")
if user not in a:
    print("Invalid input")
else:
    robo = random.choice(a)

    print("Computer's choice:", robo)

    if user == robo:
        print("It's a draw")
    elif (user == "scissor" and robo == "rock") or \
         (user == "rock" and robo == "paper") or \
         (user == "paper" and robo == "scissor"):
        print("Computer wins")
    else:
        print("hurray! You win")
                                            