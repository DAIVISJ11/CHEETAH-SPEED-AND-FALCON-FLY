  




questions = (" What is the biggest cat  that ever existed? : ",
            "What is  the smallest cat that ever existed? : ",
            "What is the only social cat? :", 
            "Can a jaguar kill a camain? :", 
            "Which is stronger tiger or a lion", 
        " wich is the strongest cat relaive  to body size  ever existed  ? :", 
            " can a tiger kill a african lion? :", 
            )

options = (("A.lion", "B. tiger", "C.smilodon", "D. giant cheetah", "E. Machairodus"),
            ("A. rusty spotteD cat", "B. himalayan persian", "C.tiger", "D. jaguar", "E.leopard"), 
            ("A. lion", "B.cheetah", "C.tiger", "D.leopard", "E. snow leopard"), 
            ("A. yes", "B. no"), 
            ("A. tiger ", "B lion")
            ("A.leopard  ", "B. snow leopard", "C. lion", "D.tiger", "E. jaguar")
            ("A. Maybe", "B. likely", "C. not likely", "D. definately", "E. no", " F.50 50"))


answers = ("E", "B", "A", "A", "A", "A", "F")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
   
    guess = input("Enter(A, B, C, D , E, F):")
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")

    else:
        print(f"{answers[question_num]} is the correct answer")

    question_num += 1

print("-------------------------")
print("          Results          ")
print("-------------------------")


print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = (score / len(question) * 100)
print(f" Your score is : {score} % ")