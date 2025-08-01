# simple quiz game 
print("Welcome to the quiz game! 🧠", "\n you will be asked 3 questions and each question carries 10 points " , "\n let's start the game")
score = 0
print("who is the founder of python? \n A) Guido van Rossum  B) Bjarne Stroustrup \n C) James Gosling  D) Dennis Ritchie \n")
answer = input("Enter your answer: ")
if answer == "A" or answer == "a" or answer == "Guido van Rossum" or answer == "guido van rossum" or answer == "A) Guido van Rossum" or answer == "guido" or answer == "A)":
    score += 10
    print("Correct! You have earned 10 points.")
else:
    print("Incorrect! The correct answer is A) Guido van Rossum.")
print("What is the capital of India? \n A) Hyderabad  B) New Delhi \n C) Mumbai  D) Bangalore \n")
answer2 = input("Enter your answer: ")
if answer2 == "B" or answer2 == "b" or answer2 == "New Delhi" or answer2 == "new delhi" or answer2 == "B) New Delhi" or answer2 == "new delhi" or answer2 == "B)":
    score += 10
    print("Correct! You have earned 10 points.")
else:
    print("Incorrect! The correct answer is B) New Delhi.")
print("Which planet is known as the Red Planet? \n A) Earth  B) Mars \n C) Jupiter  D) Saturn \n")
answer3 = input("Enter your answer: ")
if answer3 == "B" or answer3 == "b" or answer3 == "Mars" or answer3 == "mars" or answer3 == "B) Mars" or answer3 == "mars" or answer3 == "B)":
    score += 10
    print("Correct! You have earned 10 points.")
else:
    print("Incorrect! The correct answer is B) Mars.")
print(f"Your total score is: {score} out of 30")
print(" 🎉 Congratulations for completing the quiz game! 🧠 ")