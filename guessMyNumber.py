import random

print("Hello! I am thinking of a number between 1-6 and you have 4 tries to guess it!")
print("What will be your first guess?")

number = random.randint(1, 6)

for i in range(1, 4):
    print("Take a guess!")
    guess = int(input())
    if (guess == number):
        break
    elif (guess > number):
        print("Your number is too high!")
    elif (guess < number):
        print("Your number is too low!")

if (guess == number):
    print("Congratulations you got the right number!")
else:
    print("Awww you were close! The right answer was " + str(number))
