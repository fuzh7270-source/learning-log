import random

computer = random.randint(1,10)

user = int(input("Choose a number (1-10):"))

if user == computer:
    print("You win!")

else:
    print("You lose!")

print("Computer chose:", computer)


import random 

secret = random.randint(1,10)

guess = int(input("Guess the number(1-10):"))

if guess == secret:
    print("Correct!")

elif guess <secret:
    print("Too low!")

else:
    print("Too high!")

print("Answer:", secret)


import random 

secret = random.randint(1,20)

guess = int(input("Guess the number(1-20):"))

if guess == secret:
    print("Correct!")

elif guess < secret:
    print("Too low")

else:
    print("Too high")

print("Answer:", secret)
