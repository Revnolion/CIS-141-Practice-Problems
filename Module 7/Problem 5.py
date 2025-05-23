#5. Write a function called level_up(experience) that takes a player's experience
# points and returns their new level based on these rules:
# * 0-99 XP → Level 1
# * 100-199 XP → Level 2
# * 200+ XP → Level 3

# Input should be a integer
# Output should be a string
# Function body should be experience, 

def level_up(experience):
    if experience >= 0 and experience <= 99:
        print("Level 1")
    elif experience >= 100 and experience <= 199:
        print("Level 2")
    else:
        print("Level 3")
    return

level_up(8000)
