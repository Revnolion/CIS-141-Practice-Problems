#1. Create a list of integers (you get to pick!). Write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.

numbers = [2, 14, 35, 61, 100]
list_sum = 0

for number in numbers:
    if number % 2 == 0:
        list_sum += number
    
print(list_sum)


