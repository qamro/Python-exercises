questions = ("What is the best TVshow ever?: ",    
"Who is the best footballer in the history (GOAT)?: ",
"What is the worst higher school in Algeria?:",
"What is the hardest subject ever? :",
"Who is the best chess player ever (GOAT)?:",
"Who is the best anime character ever?:",
"How many tailed beasts (Biju) are there in the NARUTO anime?:")
options = (("A. Breaking Bad", "B. Prison Break", "C. Game of Thrones", "D. The Walking Dead"),
("A. Diego Armando Maradona", "B. Lionel Messi", "C. Cristiano Ronaldo", "D. PÉLE"),
("A. ENSIA", "B. ENP Alger", "C. ESI Alger", "D. ESTIN"),
("A. Algebra", "B. Algorithmic and Dynamic Data Structures", "C. Computer Architecture", "D. Analysis"),
("A. Bobby Ficher", "B. Magnus Carlsen", "C. Garry Kasparov", "D. Mikhail Tal"),
("A. Monkey D Luffy", "B. Uzumaki Naruto", "C. Kurosaki Ichigo", "D. Son Goku"),
("A. 8", "B. 9", "C. 10", "D. 11"))
answers = ("A", "C", "D", "C", "B", "A", "B")
guesses = []
question_num = 0
score = 0
for question in questions:
    print("-------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    
    guess = input("Enter (A, B, C, D): ").upper()   # i used .upper() to handle the case of "a"
    guesses.append(guess)
    if guess == answers[question_num]:
        score = score + 1
        print("CORRECT!")    
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the right answer")
    question_num = question_num + 1
    
    
print("----------------------")
print("       RESULTS        ")
print("----------------------")
print("Answers: ", end="")           
for answer in answers:
    print(answer, end=" ") 
print()
print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ") 
print()    
score = int((score / len(questions)) * 100)
print(f"Your score is: {score}%")