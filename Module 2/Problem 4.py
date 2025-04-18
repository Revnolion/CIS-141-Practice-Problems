# Create a program that prompts the user for their birth years and displays a message that says "you are ___ old". Use an f-string in your solution to this problem. 

Birth_Year = int(input("What is your birth year? "))
Current_Year = 2025

Current_Age = Current_Year - Birth_Year

print(f"You are {Current_Age} years old :)")
