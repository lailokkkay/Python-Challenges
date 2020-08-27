import random
moves = ["Rock", "Paper", "Scissors"]

playerMove = int(input("0 for Rock, 1 for Paper, 2 for Scissors : "))

computerMove = random.randint(1,2)

if computerMove == 1:
    print(moves[playerMove] + " beats " + moves[playerMove - 1] + ". You Win!")
elif computerMove == 2:
    print(moves[playerMove + 1] + " beats " + moves[playerMove] + ". You Lose!") 