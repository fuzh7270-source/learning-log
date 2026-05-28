def check_score (score):
    
    if score >= 80:
        print("Excellent")
    elif score >=60:
        print("Pass")
    else:
        print("Fail")

while True:

    try:
         user_score = int(input("Enter your score:"))
         check_score(user_score)
         break
    
    except ValueError:
        print("Please enter a number")

check_score(45)
