import random

def ask_question():
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    operation = random.choice(['+', '-', '*'])

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    user_answer = int(input(f"What is {num1} {operation} {num2}? "))
    return user_answer == correct_answer

def math_quiz():
    correct_answers = 0
    total_questions = 0

    while True:
        if ask_question():
            print("Correct!")
            correct_answers += 1
        else:
            print("Incorrect!")
        total_questions += 1
        continue_quiz = input("Do you want to continue? (yes/no): ").lower()
        if continue_quiz != "yes":
            break
    print(f"You got {correct_answers} out of {total_questions} correct.")

# Main Program
math_quiz()
