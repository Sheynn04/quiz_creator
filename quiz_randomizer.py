import random

# 1. Define how each question would output.

individual_ques = []
def questions_output():
    with open("quiz_creator.txt", "r") as quiz_file:
        lines = quiz_file.readlines()
    # Create a temporary storage for the datas that will be used.

    questions = ""
    choices = []
    answer = ""

    for line in lines:
        if line.startswith("Question"):
            questions = line.split(":", 1)[1].strip()
            choices = []

        elif line.startswith("Option"):
            choices.append(line.split(":", 1)[1].strip())

        elif line.startswith("Answer"):
            answer = line.split(":", 1)[1].strip()
            
            # This line stores all the data of a question in one variable.
            individual_ques.append({
            "question": questions,
            "choices": choices,
            "answer": answer
        })
            
    return individual_ques

# 2. Define the randizer and how options would display.

def quiz_randomizer(individual_ques):
    score = 0 
    random.shuffle(individual_ques)

    for ques_num, ques_contents in enumerate(individual_ques): # This function allows us the access each question stored in the local library we made.
        print(f"Q{ques_num +1}: {ques_contents['question']}")
        print(f"A. {ques_contents['choices'][0]}")
        print(f"B. {ques_contents['choices'][1]}")
        print(f"C. {ques_contents['choices'][2]}")
        print(f"D. {ques_contents['choices'][3]}")

        user_answer = input("Choose the letter of your answer: ").upper()

        if user_answer == ques_contents["answer"]: # Checks if the answer of the user matches the answer from the file.
            print("Correct!")
            score += 1

        else:
            print("Wrong!")
    
    print(f"Your final score is: {score} out of {len(individual_ques)}")

# 3. Call the definitions we made to start the quiz.

questions_output()
quiz_randomizer(individual_ques)


              