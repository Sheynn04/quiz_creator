import random

with open('quiz_creator.txt', 'r') as quiz_file:
    lines = quiz_file.readlines()
    print(random.choice(lines))