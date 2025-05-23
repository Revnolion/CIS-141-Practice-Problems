#4. Write a function called ferry_fare(age, vehicle) that calculates the Washington
# State Ferry fare based on age and whether the person has a vehicle. Assume the following rates:
# * Adults (19-64): $10 without a vehicle, $20 with a vehicle.
# * Seniors (65+): $5 without a vehicle, $15 with a vehicle.
# * Children (0-18): Free.

def ferry_fare(age, vehicle=False):
    if age > 18 and age < 65 and vehicle:
        print("Your fee will be $20!")
    elif age > 18 and age < 65:
        print("Your fee will be $10!")
    elif age >= 65 and vehicle:
        print("Your fee will be $15!")
    elif age >= 65:
        print("Your fee will be $5!")
    else:
        print("Your ticket is free!")
    return

ferry_fare(15, vehicle=False)
