# Prompt the user for a word. Then prompt the user for how many times they'd like that work repeated. Use the skills you learned in this module to print the word the correct number of times. 

Word = input("Please input a word, any word: ")
Repeats = input("How many times would you like this word repeated: ")
repeat_string = Word * int(Repeats)

print(repeat_string)