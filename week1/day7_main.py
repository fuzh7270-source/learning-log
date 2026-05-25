users = [
    {"name": "Alice", "age":20},
    {"name": "Bob", "age":25},
    {"name": "Charlie", "age":30}
]

for user in users:
    print(user["name"], user["age"])

users. append({"name": "David", "age":35})

print(users)

for user in users:
    if user["age"] >= 25:
        print(user["name"])

print(users)


