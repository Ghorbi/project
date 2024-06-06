import random
while True:
    user=str(input(f"Rock or paper or scissors? "))
    game=["rook","paper","scissors"]
    computer = random.choice(game)
    print(computer)
    if user =="camputer":
        print("Both players chose the same thing")
    elif user =="paper":
        if computer == "scissors":
            print("you lose!")
        else:
            print("you win!")
    elif user == "rock":
        if computer=="papar":
            print("you lose!")
        else:
            print("you win!")
    elif user =="scissors":
        if computer == "rock":
            print("you lose!")
        else:
            print("you win!")  
                        