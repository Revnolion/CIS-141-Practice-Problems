#4 Prompt the user for: a word, a first index, and a last index. Slice the word at the indexes provided by the user and print to the screen. 

word = input("Please give me a word, any word: ")
indexfirst = int(input("What is the first index? "))
indexlast = int(input("What is the last index? "))

print(word[indexfirst:indexlast])
