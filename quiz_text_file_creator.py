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



# 3. Compile the inputs into one text file. 