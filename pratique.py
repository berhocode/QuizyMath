import random
import time

def genarate_question(difficulty):
    operators = ["+", "-", "*", "/"]
    op = random.choice(operators)

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

def math_quiz():
    sentence = "Welcome to our Math Quiz Game!"
    for i in range(len(sentence)):
        print(f"\r{sentence[:i+1]}", end="")
        time.sleep(0.1)

    print()

    difficulty = input("Enter the difficulty (easy, medium, hard) > ").lower()
    if difficulty not in ["easy", "medium", "hard"]:
        print(f"{difficulty} is invalid, Defaulting to EASY...")
        difficulty = "easy"

    score = 0
    total_questions = 5

    for _ in range(total_questions):
        question, correct_answer = genarate_question(difficulty)

        try:
            user_answer = float(input(f"Solve: {question} > "))
            if user_answer == correct_answer:
                print("Correct!")
                score+=1
            else:
                print(f"Wrong, the answer was {correct_answer}")
        except ValueError:
            print("invalid input, skiping question...")

        
    print(f"Game Over!, Your total score is {score}/{total_questions}")

    repeat = input("Play again? (y/n) > ")
    if repeat.lower() == "y":
        math_quiz()
    else:
        quit()

if __name__ == "__main__":
    math_quiz()
