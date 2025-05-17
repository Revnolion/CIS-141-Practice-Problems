#4.  Create a list of integers. Write code that counts how many numbers are positive and how many are negative, then print both counts.

numbers = [3, -7, 21, 8, -8, 5, 12]
negative_numbers = 0
positive_numbers = 0

for number in numbers:
    if number > 0:
        negative_numbers += 1
    else:
        positive_numbers += 1

print(negative_numbers)
print(positive_numbers)