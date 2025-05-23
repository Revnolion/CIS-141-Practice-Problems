#1. Write a function called count_vowels(input) that takes a string and returns the number of vowels (a, e, i, o, u) in it.

# Input needs to be a string
# Output should be an integer
# Function body should be lowercase (vowels), 

def count_vowels(input = input("Please enter a sentence: ")):
    vowels = "aeiouAEIOU"
    counter = 0
    for letter in input:
        if letter in vowels:
            counter += 1
    print(counter)
    return

count_vowels()
    