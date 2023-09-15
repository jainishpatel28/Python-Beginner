# Calculator
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def calculator():
  from art import logo
  print(logo)
  user_choice = "y"
  num1 = float(input("What's the first number?: "))
  for symbol in operations:
      print(symbol)
  while user_choice == "y":
      operational_symbol = input("Pick the operation: ")
      num2 = float(input("What's the next number?: "))
    
      #below line will call the function
      function = operations[operational_symbol]
      answer = function(num1, num2)
      print(f"{num1} {operational_symbol} {num2} = {answer}")
      user_choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit and start new calculator.: ")
      if user_choice == "y":
        num1 = answer
      else:
        user_choice == "n"
        calculator()

calculator()