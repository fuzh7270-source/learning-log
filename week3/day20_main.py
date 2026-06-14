def say_hello():
    print("Hello!")

say_hello()

def get_guess():

    guess = int(input("Guess the number:"))

    return guess 

number = get_guess()

print(number)

def check_answer(guess, secret):

    if guess == secret:

        return True
    
    return False

print(check_answer(5,5))

print(check_answer(3,5))


import random

def get_guess():
    
    return int(input("Guess the number:"))

def check_answer(guess, secret):

    return guess == secret

secret = random.randint(1,20)

attempts = 0

while True:

    try: 
        guess = get_guess()
    
        attempts += 1

        if check_answer(guess, secret):

            print("Correct!")

            print("You needed", attempts, "attempts.")

            break

        else:
            print("Try again!")
    
    except:
        print("Please enter a valid number.")
