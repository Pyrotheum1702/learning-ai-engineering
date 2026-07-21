# ### 10. Quiz app with a question bank
# Load questions from a file and quiz the user.
# - **Requirements:** questions + answers stored in JSON; randomize order; support
#   multiple choice; score at the end with a percentage; handle a missing bank file.
# - **You'll learn:** loading structured data, shuffling, scoring, separating data from code.
# - **Stretch:** category selection; persist a high-score table.

import string
import random
from helper import load_data

DEV = False
FILE_NAME = "question_bank.json"

CATEGORY = "category"
QUESTION = "question"
CHOICES = "choices"
ANSWER = "answer"

choice_index = string.ascii_uppercase


def ask_quiz(i, quiz):
    try:
        if not quiz:
            print("Error: quiz is undefined")
            return False

        print(f"\n{i+1}: {quiz[QUESTION]}")

        choices = quiz[CHOICES]
        correct_answer = choices[quiz[ANSWER]]
        random.shuffle(choices)

        valid_choices = []
        choice_map = {}
        choice_parts = []

        for j, item in enumerate(choices):
            x = choice_index[j]
            valid_choices.append(x)
            choice_map[x] = j
            choice_parts.append(f"{x}: {item}")

        print("  " + "    ".join(choice_parts))

        answer = None
        while True:
            raw = input("answer: ").strip().upper()
            if raw not in valid_choices:
                print(f"Invalid answer -- valid answers: {'|'.join(valid_choices)}\n")
                continue
            answer = choice_map[raw]
            break

        print("")

        if choices[answer] == correct_answer:
            print(f"Correct.")
            return True
        else:
            print(f"Wrong! the answer is: {correct_answer}")
            return False
    except EOFError:
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False


def main():
    questions = load_data(FILE_NAME)

    if not questions:
        return print("Error: Question bank is empty or not found.")

    score = 0
    quiz_count = len(questions)
    random.shuffle(questions)

    if DEV:
        print("loaded question bank:")
        print(f"quiz_count: {quiz_count}")
        print(questions)

    for i, quiz in enumerate(questions):
        correct = ask_quiz(i, quiz)

        if correct:
            score += 1

    score_percentile = float(score) / float(quiz_count)

    print("")
    print(f"Result: {score}/{quiz_count} - {score_percentile*100:.2f}%")


main()
