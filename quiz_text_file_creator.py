# 1. Ask for the user to input the tile of the quiz. 
quiz_title = input("What is the title of this quiz?: ")

# 2. Ask how many items this quiz has.
while True:
    try:
        item_quantity = int(input("How many items does this quiz have?: "))
        break
    except ValueError:
        print("Please input a proper value!")
        continue

# 3. Create a loop that asks the user to input the questions, choices and answers to each question.

quiz_data = [] # I created this variable to check which data the system has stored.
for i in range(item_quantity):
    quiztion = input(f"Input your question {i+1}: ")

    choice_A = input("Enter choice A: ")
    choice_B = input("Enter choice B: ")
    choice_C = input("Enter choice C: ")
    choice_D = input("Enter choice D: ")

    while True:
        answer = input("Which letter is the correct answer?: ").upper()
        if answer in ["A", "B","C","D"]:
            break
        else: 
            print("Answer not int the options! Please input A,B,C or D: ")

    quiz_data.append({
        "question": quiztion,
        "choices": [choice_A, choice_B, choice_C, choice_D],
        "answer": answer
        })

print(f"\nQuiz Data Stored: {quiz_data}")


# 4. Compile the inputs into one text file. 
filename = "quiz_creator.txt"

with open(filename, "w", encoding="utf-8") as f:
    f.write(f"Quiz Title: {quiz_title.title()}\n\n")
    f.write(f"Quiz Item Quantity: {item_quantity}\n\n")   

    for i, item in enumerate(quiz_data):
        f.write(f"Question {i+1}: {item['question']}\n")

        f.write(f"  Option A: {item['choices'][0]}\n")  # Print choice A
        f.write(f"  Option B: {item['choices'][1]}\n")  # Print choice B
        f.write(f"  Option C: {item['choices'][2]}\n")  # Print choice C
        f.write(f"  Option D: {item['choices'][3]}\n")  # Print choice D

        f.write(f"Answer: {item['answer']}\n\n")

print(f"Quiz saved to '{filename}' successfully!")