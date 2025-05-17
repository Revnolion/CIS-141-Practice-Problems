#5. Create a list of integers. Use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.

numbers = [2, 6, 7, 12, 14]
squared_list = []

for number in numbers:
    squared_list.append(number**2)

print(squared_list)
