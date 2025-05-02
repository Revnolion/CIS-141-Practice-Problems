#4. A theater wants to enforce age restrictions for movie tickets. Ask the user for their age, and tell them whether they can see G (appropriate for under 13), PG-13 (appropriate for 13 to 17), or R (appropriate for over 18) rated movies.

current_age = int(input("What is your current age? "))

if current_age < 13:
    print("You can see G-rated movies")
elif current_age > 13 and current_age < 17:
    print("You can see G-rated and PG-13-rated movies")
else:
    print("You can see G-rated, PG-13-rated, and R-rated movies")