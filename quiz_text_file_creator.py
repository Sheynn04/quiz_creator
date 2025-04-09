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


# 3. Compile the inputs into one text file. 