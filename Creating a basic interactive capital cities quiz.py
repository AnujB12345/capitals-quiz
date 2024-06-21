import tkinter as tk
import random
from tkinter import messagebox
from tkinter import PhotoImage
from data import capitals

def open_main_window():
    menu_window.destroy()

    root = tk.Tk()
    root.title("Capital Cities Quiz")

    icon = PhotoImage(file='logo.png')
    root.iconphoto(True, icon)

    window_width = 800
    window_height = 400
    root.configure(bg="#f0f0f0")  # Light gray background
    root.resizable(False, False)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    center_x = int(screen_width / 2 - window_width / 2)
    center_y = int(screen_height / 2 - window_height / 2)

    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

    countries = list(capitals.keys())

    correct_answers = 0
    wrong_answers = 0
    total_questions = 0

    def start_quiz():
        nonlocal correct_answers, wrong_answers, total_questions
        correct_answers = 0
        wrong_answers = 0
        total_questions = 0
        ask_questions()

    def ask_questions():
        nonlocal total_questions
        total_questions += 1

        random_country = random.choice(countries)
        corresponding_capital = capitals[random_country]

        question_label.config(text=f"What is the capital city of {random_country}?", font=('Arial', 18, "bold"))

        def check_answer():
            nonlocal correct_answers, wrong_answers
            user_guess = entry.get().title().strip()

            if user_guess == corresponding_capital:
                messagebox.showinfo("Correct", "Well done, you got it right!")
                correct_answers += 1
            else:
                messagebox.showerror("Incorrect",
                                     f"Unfortunately, you got it wrong. The correct answer is {corresponding_capital}")
                wrong_answers += 1

            ask_questions()
            entry.delete(0, tk.END)
            entry.focus()

        submit_button.config(command=check_answer, bg="#4CAF50", fg="white", font=('Arial', 14, 'bold'))
        quit_button.config(bg="#F44336", fg="white", font=('Arial', 14, 'bold'))

    def quit_quiz():
        nonlocal total_questions, correct_answers, wrong_answers
        total_questions -= 1
        try:
            percent = (correct_answers / total_questions) * 100
            messagebox.showinfo("End of Quiz",
                                f"Quiz ended.\n\nTotal Questions: {total_questions}\nCorrect Answers: {correct_answers}\nWrong Answers: {wrong_answers}\nPercentage score: {percent:.2f}%")
        except ZeroDivisionError:
            messagebox.showinfo("End of Quiz",
                                f"Quiz ended.\n\nTotal Questions: {total_questions}\nCorrect Answers: {correct_answers}\nWrong Answers: {wrong_answers}\nPercentage score: 0%")
        root.destroy()

    question_label = tk.Label(root, text="", font=('Arial', 18, "bold"), padx=20, pady=20, bg="#f0f0f0")
    question_label.pack()

    entry = tk.Entry(root, width=30, font=('Arial', 14))
    entry.pack(pady=10)

    submit_button = tk.Button(root, text="Submit Answer", command=ask_questions, font=('Arial', 14, 'bold'))
    submit_button.pack(pady=10)

    quit_button = tk.Button(root, text="Quit", command=quit_quiz, font=('Arial', 14, 'bold'))
    quit_button.pack(pady=10)

    ask_questions()

    root.mainloop()


menu_window = tk.Tk()
menu_window.title("Quiz Menu")

icon = PhotoImage(file='logo.png')
menu_window.iconphoto(True, icon)

window_width = 700
window_height = 300
menu_window.configure(bg="#f0f0f1")  # Light gray background
menu_window.resizable(False, False)

screen_width = menu_window.winfo_screenwidth()
screen_height = menu_window.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

menu_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

label_menu = tk.Label(menu_window, text="Welcome to the Capital Cities Quiz", font=('Arial', 20, "bold"), bg="#f0f0f0")
label_menu.pack(pady=50)

start_button = tk.Button(menu_window, text="Start Quiz", font=('Arial', 20, 'bold'), command=open_main_window, bg="#4CAF50", fg="white", padx=20, pady=10)
start_button.pack()

menu_window.mainloop()
