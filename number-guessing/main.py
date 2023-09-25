#Number Guessing Game Objectives:

#print LOGO
import random
from art import logo
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