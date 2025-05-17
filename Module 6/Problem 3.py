#3. Create a list of strings. Write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.

strings = ["Hi", "How", "Are", "You", "I'm", "Good", "Thank", "You"]
new_list = []

for string in strings:
    if len(string) > 3:
        new_list.append(string)
    
print(new_list)