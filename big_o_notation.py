# Time Complexity of below code is O(n) It will depend on the size of the list.
# It will take the number from list and print the square of them.
def get_squared_numbers(number):
    squared_numbers = []
    for n in number:
        squared_numbers.append(n*n)
    return squared_numbers


numbers = [2, 5, 8, 9]
print(f"Squares of numbers in list are: {get_squared_numbers(numbers)}")

# Time Complexity of below code is O(n²)
# It will print the duplicated number in the list.
numbers = [3, 6, 2, 4, 3, 6, 8, 9]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(f"Duplicated number in this list is: {numbers[i]}")
            break
