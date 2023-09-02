rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
user = int(input("What do you choose? type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
shapes = [rock, paper, scissors]
player = shapes[user]
print(shapes[user])

# Computer choice
computer = random.choice(shapes)
print("Computer chose:\n" + computer)

# Comparison of both choices
# What if player enter wrong number
if player == rock and computer == scissors:
  print("You win.")
elif player == scissors and computer == paper:
  print("You win.")
elif player == paper and computer == rock:
  print("You win.")
elif player == computer:
  print("Match draw.")
else:
  print("You lose.")