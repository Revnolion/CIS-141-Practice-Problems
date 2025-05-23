#3. In the game Pokemon, certain types of Pokemon do extra damage to other types.
# For example, water is very effective to fight fire.
# Write a function called type_advantage(attacker, defender) that takes two Pokémon types as
# strings and returns "Super Effective", "Not Very Effective", or "Neutral" based on
# simple type effectiveness rules. Your solution only needs to work for these three sets of input:
# print(type_advantage("Water", "Fire")) # "Super Effective"
# print(type_advantage("Fire", "Water")) # "Not Very Effective"
# print(type_advantage("Electric", "Grass")) # "Neutral"

def type_advantage(attacker= "", defender= ""):
    if attacker == "Grass" and defender == "Electric":
        print("Neutral!")
    elif attacker == "Fire" and defender == "Water":
        print("Not Very Effective!")
    elif attacker == "Water" and defender == "Fire":
        print("Super Effective!")
    return

type_advantage("Grass", "Electric")