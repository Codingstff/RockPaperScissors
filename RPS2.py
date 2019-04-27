import random

def beats(a,b):
    return (b == "rock" and a == "paper") or (b == "paper" and a == "scissors") or (b == "scissors" and a == "rock")

def show_picks(computer,player):
    print ("The computer chose",computer, "you chose",player)

def show_result(player,computer):
    if beats(player,computer):
        print ("you win")
    
    elif beats(computer,player):
        print ("you lose")

    elif (computer == player) :
        print ("draw try again")

    else:
        print("Not a valid input, try again")

def show_intro():
    print()
    print("Are you ready for rock, paper, scissors?")
    print("Do you think you can defeat the computer?")

def take_player_input():
    choice = input("Lets begin rock, paper or scissors? ")
    choice = choice.strip()
    return choice

def generate_computer_choice():
    RPS = ["rock","paper","scissors"]
    computer = random.choice(RPS)
    return computer
    
    
    
while True:
    show_intro()
    
    player = take_player_input()

    computer = generate_computer_choice()

    show_picks(computer, player)

    show_result(player,computer)

    
