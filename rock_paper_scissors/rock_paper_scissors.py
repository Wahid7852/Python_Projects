import random


def play():
    player = input("Choose 'r' for Rock, 'p' for Paper and 's' for seciorrs\n")
    computer = random.choice(['r','p','s'])
    
    # When draw occurs
    if player==computer:
        print("\nMatch Draw")

    # When player chooses rock
    elif (player=='r'):
        if computer=='p':
            print("\nComputer WINS")
        else:
            print("\nPlayer WINS")

    # When player chooses paper
    elif player=='p':
        if computer=='r':
            print("\nPlayer WINS")
        else:
            print("\nComputer WINS")

    # When player chooses scissor
    elif player=='s':
        if computer=='r':
            print("\nComputer WINS")
        else:
            print("\nPlayer WINS")
            
    print(f"You have choosen {player} and the computer has choosen {computer} ")

    
play()

