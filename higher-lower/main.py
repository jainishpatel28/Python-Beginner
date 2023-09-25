'''creating Higher-Lower game'''

#imports
import art
import game_data
import random
from replit import clear


def compare_values(compareA, compareB):
  '''comparing two values'''
  a = compareA['follower_count']
  b = compareB['follower_count']
  if a > b:
    return "A"
  elif b > a:
    return "B"

def generate_stat():
  '''function to generate random choice of list'''
  a = random.choice(game_data.data)
  return a

def true_value(valueOne, valueTwo):
  '''function if user got it right so converting A to B and assigning B new value'''
  valueOne = valueTwo
  valueTwo = generate_stat()
  return valueOne, valueTwo

def make_str(a):
  '''function to format statements and print'''
  account_name = a["name"]
  account_description = a["description"]
  account_country = a["country"]
  return f"{account_name}, {account_description}, from {account_country}"


right_add = 0 
print(art.logo)
first_choice = generate_stat()

keep_going = True
while keep_going:
  print(f"Compare A: {make_str(first_choice)}.")
  print(art.vs)
  second_choice = generate_stat()
  if second_choice == first_choice:
    second_choice = generate_stat()
  print(f"Compare B: {make_str(second_choice)}.")
  
  winner = compare_values(first_choice, second_choice)
  user_entry = input("Who has more followers? Type 'A' or 'B': ")
  clear()
  print(art.logo)
  
  #adding if-else to check answer right or wrong
  if winner == user_entry:
    first_choice = second_choice  
    right_add += 1
    print(f"You're right! Current score: {right_add}")
  else:
    keep_going = False
    print(f"Sorry, that's wrong. Final score: {right_add}")