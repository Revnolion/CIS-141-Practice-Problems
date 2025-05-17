#2. Create a list of strings. Write code that counts how many times the word "Olympic" appears in the list, and then print the count.

strings = ["College", "Olympic", "Olympic", "Mountains", "Cascade Mountains"]

total_olympic = 0

for word in strings:
    if word == "Olympic":
        total_olympic += 1
    
print((total_olympic))