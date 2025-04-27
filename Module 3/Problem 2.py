# #2. Prompt the user for their name and their age. Calculate their age next year. Use string concatenation to print "Hello, <name>! You are <age1> years old. Next year, you will be <age2> years old."

name = input("Please give me your name: ")
current_age = int(input("What is your current age: "))
next_age = current_age + 1

print("Hello, " + name + "! You are " + str (current_age) + "years old. Next year, you will be " + str(next_age) + " years old.")