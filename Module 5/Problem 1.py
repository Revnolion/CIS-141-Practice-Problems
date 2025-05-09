#1. Prompt the user for a positive integer n. Use a while loop to sum all the integers from 1 up to n. Print the final sum.

number = int(input("Please give me a positive integer: "))
count = 1
sum = 0


while count <= number:
    sum += count
    count += 1
print(sum)