import tkinter as tk
from tkinter import messagebox

# Quiz Data
questions = [
    "How many continents are there in the world?",
    "What is the full meaning of CPU?",
    "Which planet in the solar system is the largest?",
]

options = [
    ["7", "6", "5", "4"],
    ["Central Process Unit", "Center Processing Unit", "Central Processing Unit", "Car Parking Unit"],
    ["Mercury", "Jupiter", "Venus", "Mars"],
]

answers = ["A", "C", "B"]

# Initialize variables
current_question = 0
score = 0
user_answers = []

# Function to check the answer
def check_answer(selected_option):
    global current_question, score

    if selected_option == answers[current_question]:
        score += 1

    user_answers.append(selected_option)

    if current_question < len(questions) - 1:
        current_question += 1
        display_question()
    else:
        display_results()

# Function to display a question
def display_question():
    question_label.config(text=questions[current_question])

    # Update button texts
    for i, option in enumerate(options[current_question]):
        option_buttons[i].config(text=f"{chr(65 + i)}. {option}")

# Function to display results
def display_results():
    result_text = f"Your Score: {score}/{len(questions)}\n\n"
    for i in range(len(questions)):
        result_text += f"Q{i+1}: {questions[i]}\nYour Answer: {user_answers[i]}\nCorrect Answer: {answers[i]}\n\n"

    # Show results in a message box
    messagebox.showinfo("Quiz Results", result_text)
    root.destroy()

# GUI Setup
root = tk.Tk()
root.title("Quiz Game")
root.geometry("600x400")
root.resizable(False, False)

# Question Label
question_label = tk.Label(root, text="", font=("Arial", 16), wraplength=500, justify="center")
question_label.pack(pady=20)

# Option Buttons
option_buttons = []
for i in range(4):
    btn = tk.Button(root, text="", font=("Arial", 14), width=20, command=lambda opt=chr(65 + i): check_answer(opt))
    btn.pack(pady=5)
    option_buttons.append(btn)

# Start the quiz
display_question()

# Run the GUI
root.mainloop()
