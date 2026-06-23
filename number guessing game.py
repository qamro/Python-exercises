import random
lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
print("---------Number Guessing Game---------")
print(f"Select a number between {lowest_num} and {highest_num}")
while True:
    guess = input("Enter your guess: ")
    if guess.isdigit():
        guess = int(guess)
        guesses = guesses + 1
        if guess < lowest_num or guess > highest_num:
            print("The number is out of range")
            print(f"Please Select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try again!")    
        elif guess > answer:
            print("Too high! Try again!")  
        else:
            print(f"🎉🎉🎉CORRECT! The answer was {answer}")  
            print(f"Number of guesses is {guesses}")  
            play_again = input("Play again?(Enter YES or NO): ")
            if play_again.upper() == "NO":
                break
            else:
                answer = random.randint(lowest_num, highest_num)
                guesses = 0    
                print("---------Number Guessing Game---------")
                print(f"Select a number between {lowest_num} and {highest_num}")
    
    else:
        print("Invalid guess") 
        print(f"Please Select a number between {lowest_num} and {highest_num}")   