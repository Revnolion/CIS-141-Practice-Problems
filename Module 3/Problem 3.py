# 3 Prompt the user for a sentence and a word to try to find in that sentence. Have the program print out whether the word was found in the sentence. (i.e. True or False)

sentence = input("Please type a full sentence: ")
word_to_find = input("What word in this sentence would you like to find: ")

print(word_to_find in sentence)