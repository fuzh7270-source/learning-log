import random

secret = random.randint(1,20)

attempts = 0

while True:
   
    try:
        guess = int(input("Guess the number(1-20)"))

        attempts += 1

        if guess == secret:

            print("Correct!")
            print("You needed", attempts, "attempts.")
            break

        elif guess < secret:

            print("Too low!")

        else:

            print("Too high!")

    except:
        print("Please enter a valid number.")



