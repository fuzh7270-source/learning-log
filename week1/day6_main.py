def greet():
    print("Hello")

greet()
greet()
greet()

def greet(name):
    print("Hello", name)

greet("Alice")
greet("Bob")

def say_food(food):
    print("I like", food)

say_food("Pizza")
say_food("Sushi")


book = {
    "title": "Harry Potter",
    "author": "Rowling"
}
print(book)

print(book["title"])

book["year"] = 1997

print(book)

