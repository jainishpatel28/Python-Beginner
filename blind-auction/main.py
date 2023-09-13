from replit import clear
from art import logo
print(logo)
print("Welcome to the sercet auction program.")

bids = {}
check = "yes"
while check == "yes":
  key = input("What is your name?: ")
  price = int(input("What's your bid?: $"))
  check = input("Are there any other bidders? Type 'yes' or 'no'\n")
  bids[key] = price
  clear()

null = 0
name = ""
for key in bids:
  if bids[key] > null:
    null = bids[key]
    name = key

print(f"The winner is {name} with a bid of ${null}.")