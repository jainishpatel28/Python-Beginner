#Number Guessing Game Objectives:

import random

logo = '''
 _____                  _____                      _   _     _              
|_   _|                /  ___|                    | | | |   (_)             
  | |_   _ _ __   ___  \ `--.  ___  _ __ ___   ___| |_| |__  _ _ __   __ _  
  | | | | | '_ \ / _ \  `--. \/ _ \| '_ ` _ \ / _ \ __| '_ \| | '_ \ / _` | 
  | | |_| | |_) |  __/ /\__/ / (_) | | | | | |  __/ |_| | | | | | | | (_| | 
  \_/\__, | .__/ \___| \____/ \___/|_| |_| |_|\___|\__|_| |_|_|_| |_|\__, | 
      __/ | |                                                         __/ | 
     |___/|_|                                                        |___/  
'''
print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 to 100.")

#number guessed by computer
random_number = random.randint(1, 100)

difficulty = input("Choose difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
elif difficulty == "hard":
  attempts = 5

start_number = attempts
for chances in range(attempts):
  print(f"you have {start_number} attempts remaining to guess the number.")
  start_number -= 1
  guess_number = int(input("Make a guess: "))

  if guess_number == random_number:
    print(f"You got it! The answer was {random_number}.")
    break
  elif start_number == 0:
    print("You've run out of guesses, you lose.")
  elif guess_number < random_number:
    print("Too Low.")
    print("Guess Again.")
  elif guess_number > random_number:
    print("Too High.")
    print("Guess Again.")   