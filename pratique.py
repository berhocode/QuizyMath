# Math Quiz Game, By Aymane Berhoua (@berhocode)

# importing modules:
import random
import time

# Generating Question Function:
def generate_question(difficulty):
    operations = ["+", "-", "*", "/"]
    op = random.choice(operations)

    if difficulty == "easy":
        num1, num2 = random.randint(1, 10), random.randint(1, 10)
    elif difficulty == "medium":
        num1, num2 = random.randint(10, 50), random.randint(10, 50)
    else: # hard
        num1, num2 = random.randint(50, 100), random.randint(1, 100)

    if op == "/" and num2 == 0:
        num2 = 1

    question = f"{num1} {op} {num2}"
    answer = eval(question)
    return question, round(answer, 2)


# Math Quiz Game Function:
def math_quiz():
    # Welcoming the user:
    sentence =  "Welcome To Our Math Quiz!"
    for i in range(len(sentence)):
        print(f"\r{sentence[:i+1]}", end=" ")
        time.sleep(0.1)
    print()

    # Choosing difficulty:
    difficulty = input("Enter the difficulty (easy, medium, hard) > ").lower()
    if difficulty not in ["easy", "medium", "hard"]:
        print("invalid input!, defaulting to EASY...")
        difficulty = "easy"

    total_questions = 5
    score = 0

    # Game loop
    for _ in range(total_questions):
        question, correct_answer = generate_question(difficulty)
        try:
            answer = float(input(f"Solve: {question} > "))
            if answer == correct_answer:
                print("Correct!")
                score+=1
            else:
                print(f"Wrong, the answer was {correct_answer}")
        except ValueError:
            print("Invalid input!, Skiping question...")

    print(f"Game Over!, Your score is {score}/{total_questions}")

    # ask user to Play again:
    stay = input("Play again? (y/n) > ").lower()
    if stay == "y":
        math_quiz()
    else:
        exit_game = "Exiting Program..."
        for i in range(len(exit_game)):
            print(f"\r{exit_game[:i+1]}", end=" ")
            time.sleep(0.1)
        print()
        quit()

if __name__ == "__main__":
    math_quiz()
