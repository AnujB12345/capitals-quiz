import tkinter as tk
from tkinter import messagebox
import random
import time
import os
from data import capitals

# Function to normalize the input
def normalize(text):
    return ' '.join(text.strip().lower().split())

# Function to read high scores from a file
def read_high_scores(filename='high_scores.txt'):
    if not os.path.exists(filename):
        return []
    
    with open(filename, 'r') as file:
        high_scores = [line.strip().split(':') for line in file.readlines()]
        high_scores = [(name, int(score)) for name, score in high_scores]
    return high_scores

# Function to write high scores to a file
def write_high_scores(high_scores, filename='high_scores.txt'):
    with open(filename, 'w') as file:
        for name, score in high_scores:
            file.write(f"{name}:{score}\n")

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Capital Cities Quiz")
        
        self.score = 0
        self.total_questions = 0
        self.time_limit = 10  # Time limit in seconds for each question
        
        self.countries = list(capitals.keys())
        self.current_country = None
        self.correct_capital = None
        self.start_time = None

        # GUI Elements
        self.question_label = tk.Label(root, text="Press 'Start Quiz' to begin", font=('Helvetica', 16))
        self.question_label.pack(pady=20)
        
        self.answer_entry = tk.Entry(root, font=('Helvetica', 14))
        self.answer_entry.pack(pady=10)
        
        self.submit_button = tk.Button(root, text="Submit Answer", command=self.check_answer, font=('Helvetica', 14))
        self.submit_button.pack(pady=10)
        
        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz, font=('Helvetica', 14))
        self.start_button.pack(pady=10)
        
        self.score_label = tk.Label(root, text="Score: 0", font=('Helvetica', 14))
        self.score_label.pack(pady=10)

    def start_quiz(self):
        self.score = 0
        self.total_questions = 0
        self.ask_question()
        
    def ask_question(self):
        self.current_country = random.choice(self.countries)
        self.correct_capital = capitals[self.current_country]
        self.question_label.config(text=f"What is the capital of {self.current_country}?")
        self.answer_entry.delete(0, tk.END)
        self.start_time = time.time()
        
    def check_answer(self):
        end_time = time.time()
        time_taken = end_time - self.start_time
        
        if time_taken > self.time_limit:
            messagebox.showinfo("Time's Up", f"Time's up! You took {time_taken:.2f} seconds, which is more than the {self.time_limit} second limit.")
            self.end_quiz()
            return
        
        user_answer = self.answer_entry.get().strip()
        normalized_user_answer = normalize(user_answer)
        normalized_correct_capital = normalize(self.correct_capital)
        
        if normalized_user_answer == normalized_correct_capital:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            messagebox.showinfo("Correct!", "Correct!")
        else:
            messagebox.showinfo("Wrong!", f"Wrong! The correct answer is {self.correct_capital}.")
        
        self.total_questions += 1
        self.ask_question()
        
    def end_quiz(self):
        high_scores = read_high_scores()
        
        if not high_scores or self.score > min(score for _, score in high_scores) or len(high_scores) < 10:
            player_name = tk.simpledialog.askstring("High Score", "Congratulations! You have a high score! Enter your name:")
            high_scores.append((player_name, self.score))
            high_scores = sorted(high_scores, key=lambda x: x[1], reverse=True)[:10]  # Keep top 10 scores
            write_high_scores(high_scores)
        
        self.display_high_scores(high_scores)
        
    def display_high_scores(self, high_scores):
        high_score_text = "High Scores:\n"
        for name, score in high_scores:
            high_score_text += f"{name}: {score}\n"
        messagebox.showinfo("High Scores", high_score_text)
        self.root.destroy()

# Create the main window
root = tk.Tk()
quiz_game = QuizGame(root)
root.mainloop()
