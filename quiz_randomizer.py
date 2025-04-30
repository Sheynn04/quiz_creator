import random

# 1. Define how each question would output.

def questions_output(quiz_file):
    with open("quiz_creator.txt", "r") as quiz_file:
        lines = quiz_file.readlines()
    # Create a temporary storage for the datas that will be used.
    individual_ques = []
    questions = ""
    choices = []
    answer = ""

    for line in lines:
        if line.startswith("Question"):
            questions = line.split(":",1).strip()
            choices = []

        elif line.startswith("Option"):
            choices.append(line.split(":").strip())

        elif line.startswith("Answer"):
            answer = line.split(":").strip()
            
            # This line stores all the data of a question in one variable.
            individual_ques.append({
            "question": questions,
            "choices": choices,
            "answer": answer
        })
            
    return individual_ques
