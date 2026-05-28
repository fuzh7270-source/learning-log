try:
    age = int(input ("Enter your age:"))
    print(age)
except:
    print("Please enter a number")
    

while True: 

    try:
        number = int(input("Enter number: "))
        print(number)
        break
    except:
        print("Error! Please enter a number")


try: 
    score = int(input("Enter your score:"))
    print(score)
    if score >= 80:
        print("Success!")
    else:
        print("Try again!")

except ValueError:
    print("Please enter your score")

    
