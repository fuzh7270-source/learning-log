file = open ("memo.txt", "w")
file.write("Hello, Python!")
file.close()

file = open ("memo.txt", "r")
content = file.read()
print(content)
file.close()

file = open ("memo.txt", "a")
file.write("\nNew message")
file.close()

file = open ("memo.txt", "a")
file.write("\nPizza")
file.close()

file = open ("memo.txt", "r")
content = file.read()
print(content)
file.close()
