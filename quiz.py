import random
import time
from data import capitals
countries = list(capitals.keys())

correct_answers = 0
wrong_answers = 0
total_questions = 0

def random_country():
   random_country = random.choice(countries)
   corresponding_capital= capitals[random_country]
   main(random_country, corresponding_capital)

def main(random_country, corresponding_capital):
   global correct_answers, wrong_answers, total_questions
   user_guess = input(f"What is the capital city of {random_country}: ").strip().title()
   if user_guess == corresponding_capital:
      print("Well done, you got it right!")
      correct_answers += 1
   else:
      print("Unfortunately, you got it wrong")
      wrong_answers +=1
   total_questions += 1
   time.sleep(1)
   play_again()

def play_again():
   global correct_answers, wrong_answers, total_questions
   again = input("Press any key to play again or 1 to quit")
   if again == "1":
      print("Hope you enjoyed the game, goodbye!")
      time.sleep(0.6)
      print(f"Out of {total_questions} questions,you got {correct_answers} correct answers and {wrong_answers} wrong answers. Well done")
      exit()
   else:
      random_country()

name = input("Enter your name: ").title().strip()
print(f"Hello {name}, you will be playing a capital city game. Your points will be recorded. Good luck!")
time.sleep(0.5)
random_country()
