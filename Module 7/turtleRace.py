import turtle
import random

player_one = turtle.Turtle()
player_one.color("green")
player_one.shape("turtle")
player_one.penup()
player_one.goto(-200,100)
player_two = player_one.clone()
player_two.color("blue")
player_two.penup()
player_two.goto(-200,-100)

#coordiantes
startX = -200
homeX = 300
homeRadius = 40
homeCircle = homeX - homeRadius
#set positions
player_one.goto(homeX,60)
player_one.pendown()
player_one.circle(homeRadius)
player_one.penup()
player_one.goto(startX,100)
player_two.goto(homeX,-140)
player_two.pendown()
player_two.circle(homeRadius)
player_two.penup()
player_two.goto(startX,-100)

die = [1,2,3,4,5,6]

for x in range(1,21):
    #Player 1 - Turn Start
    p1Input = input("(Player1) Press Enter to roll the die:")
    dice_outcome = random.choice(die)
    print("You rolled a", dice_outcome)
    dice_outcome *= 20
    player_one.forward(dice_outcome)
    p1Position = player_one.position()
    #Checks if Player 1 has won
    if(p1Position[0] >= homeCircle):
        print("Player 1 has reached their home.")
        break
    #Player 1 - Turn End
    #Player 2 - Turn Start
    p2Input = input("(Player2) Press Enter to roll the die:")
    dice_outcome = random.choice(die)
    print("You rolled a", dice_outcome)
    dice_outcome *= 20
    player_two.forward(dice_outcome)
    p2Position = player_two.position()
    #Checks if Player 2 has won
    if(p2Position[0] >= homeCircle):
        print("Player 2 has reached their home.")
        break
    #Player 2 - Turn End
