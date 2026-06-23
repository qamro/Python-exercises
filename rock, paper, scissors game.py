import random
options = ("rock", "paper", "scissors")
player = None
computer = random.choice(options)
while player not in options:
    print("---------Rock Paper Scissors Game---------")
    player = input("Enter a choice (rock, paper, scissors): ")    
    print(f"Player: {player}")
    print(f"Computer: {computer}")
    if player == computer:
        print("It's a tie!")
    elif player == "rock" and computer == "paper":
        print("You lose!") 
    elif player == "rock" and computer == "scissors":
        print("You win!")
    elif player == "paper" and computer == "rock":
        print("You win!")   
    elif player == "paper" and computer == "scissors":
        print("You lose!") 
    elif player == "scissors" and computer == "rock":
        print("You lose!")                 
    elif player == "scissors" and computer == "paper":
        print("You win!")   
    play_again = input("Play again?(Enter YES or NO) :") 
    if play_again.upper() == "NO":
        break
    else:
        computer = random.choice(options)
        player = None
            
