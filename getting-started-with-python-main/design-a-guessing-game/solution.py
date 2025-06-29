import random

random_number = random.randrange(100)

correct_guess = False

while not correct_guess:
    user_input = input("Guess a number between 0 and 100: ")

    try:
      number = int(user_input)
      if number == random_number:
        correct_guess = True
      elif number > random_number:
        print("You guessed too high!")
      elif number < random_number:
        print("You guessed too low!")
    except:
      print("Please enter a number :)")

print("You guessed the right number!")