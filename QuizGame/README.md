# Quiz Game

A simple True/False Quiz Game built with Python. The project uses classes and separate Python modules to organize the questions, quiz logic, and main program.

# How It Works

# The program:

Gets the questions from data.py.
Creates Question objects using question_model.py.
Stores all the questions in a question bank.
Uses the QuizBrain class to:
Display each question.
Get the user's answer.
Check whether the answer is correct.
Keep track of the score.
Displays the final score when all questions have been answered.
Project Structure
quiz-game/
│
├── main.py
├── quiz_brain.py
├── question_model.py
└── data.py
main.py

# How to Run

Make sure Python is installed, then run:

python main.py

# Example

Q.1: A slug's blood is green. (True/False): true
You got it right!
The correct answer was: True
Your current score is: 1/1

Q.2: The loudest animal is the African Elephant. (True/False): true
You got it wrong!
The correct answer was: False
Your current score is: 1/2

# At the end:

You've completed the quiz!
Your final score is: 8/12

# Concepts Practiced

Classes and objects
Constructors (__init__)
Instance attributes
Methods
Lists and dictionaries
Loops
Functions
Imports and modules
Object-oriented programming
User input and conditional statements