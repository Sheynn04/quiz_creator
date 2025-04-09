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

# 2. Create a loop that asks the user to input the questions, choices and answers to each question.
quiz_data = []
for i in range(item_quantity):
    quiztion = input(f"Input your question {i+1}: ")
    for options in range(4):
        choice = input(f"Enter choice {chr(65 + options)}: ")
    while True:
        answer = input("Which letter is the correct answer?: ").upper()
        if answer in ["A", "B","C","D"]:
            break
        else: 
            print("Answer not int the options! Please input A,B,C or D: ")

quiz_data.append({
        "question": quiztion,
        "choices": choice,
        "answer": answer
                })




# 3. Compile the inputs into one text file. 
filename = "quiz_creator.txt"
with open(filename, "w") as f:
    f.write(f"Quiz Title: {quiz_title}\n")
    f.write(f"Quiz Item Quantity: {item_quantity}\n")
    for i, item in enumerate(quiz_data):
        f.write(f"Question {i+1}: {item['question']}\n")
        for j, item in enumerate(quiz_data):
            f.write(f"Option {chr(65 + options)}: {item['choices']}\n")
        f.write(f"Answer: {item['answer']}\n")