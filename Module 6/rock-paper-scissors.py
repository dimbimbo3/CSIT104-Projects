import random

list_of_choices = ["rock", "paper", "scissors"]
cont = True
userWin = 0
compWin = 0

while(cont):
    computer = random.choice(list_of_choices)
    choice = input("Enter your choice - rock, paper, scissors (or quit):")
    if(choice.upper() == "ROCK"):
        if(computer == "paper"):
            print("You lose.")
            compWin += 1
        elif(computer == "scissors"):
            print("You win.")
            userWin += 1
        elif(computer == "rock"):
            print("It's a draw.")
    elif(choice.upper() == "PAPER"):
        if(computer == "paper"):
            print("It's a draw.")
        elif(computer == "scissors"):
            print("You lose.")
            compWin += 1
        elif(computer == "rock"):
            print("You win.")
            userWin += 1
    elif(choice.upper() == "SCISSORS"):
        if(computer == "paper"):
            print("You win.")
            userWin += 1
        elif(computer == "scissors"):
            print("It's a draw.")
        elif(computer == "rock"):
            print("You lose.")
            compWin += 1
    elif(choice.upper() == "QUIT"):
        cont = False
        print("FINAL SCORE:")
    else:
        print("Invalid input!")
        
    print("Win Total - User:", userWin, " Computer:", compWin)
