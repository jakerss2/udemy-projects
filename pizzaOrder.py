#Code comes from 100 days of code by Angela Yu implementation by me
print("Thank you for choosing Python Pizza Deliveries!")
size = input() # What size pizza do you want? S, M, or L
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

price = 0

match size:
  case "S":
    price += 15
  case "M":
    price += 20
  case "L":
    price += 25
  case _:
    print("Incorrect Size")

if add_pepperoni == "Y":
  if price >= 20:
    price += 3
  else:
    price += 2

if extra_cheese == "Y":
  price += 1

print(f"Your final bill is: ${price}.")
