"""
    1. In Feb, how many dollars you spent extra compare to January?
    2. Find out your total expense in first quarter (first three months) of the year.
    3. Find out if you spent exactly 2000 dollars in any month
    4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
    5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
"""
expenses = [
    {"January": 2200},
    {"February": 2350},
    {"March": 2600},
    {"April": 2130},
    {"May": 2190}
]

# First Question
total_expense = 0
for expense in expenses:
    total_expense += expense.get('February', 0) - expense.get('January', 0)

print(f"You spent extra {total_expense} dollars in February more than January.")

# Second Question
expense_quarter = 0
for expense in expenses:
    expense_quarter += expense.get('January', 0) + expense.get('February', 0) + expense.get('March', 0)
    
print(f"Total expense in first quarter of the year is: {expense_quarter} dollars.")

# Third Question
for expense in expenses:
    for month, amount in expense.items():
        if amount == 2000:
            print(f"You spent exactly 2000 dollars in {month}.")
            break
print("You did not spent 2000 dollar in any months.")

# Fourth Question
expenses.append({"June": 1980})
print(expenses)

# Fifth Question
expenses[3]["April"] -= 200
print(expenses)

"""
    1. Length of the list
    2. Add 'black panther' at the end of this list
    3. You realize that you need to add 'black panther' after 'hulk', so remove it from the list first and then add it after 'hulk'
    4. Now you don't like thor and hulk because they get angry easily. So you want to remove thor and hulk from list and replace them with doctor strange (because he is cool). Do that with one line of code.
    5. Sort the heroes list in alphabetical order (Hint. Use dir() functions to list down all functions available in list)
"""

heroes = ["spider man", "thor", "hulk", "iron man", "captain america"]

# First Question
print(len(heroes))

# Second Question
heroes.append("black panther")
print(heroes)

# Third Question
heroes.remove("black panther")
heroes.insert(3, "black panther")
print(heroes)

# Fourth Question
heroes[1:3] = ["doctor strange"]
print(heroes)

# Fifth Question
heroes.sort()
print(heroes)

"""
Create a list of all odd numbers between 1 and a max number.
Max number is something you need to take from a user using input() function
"""

odd_numbers = []
max_number = int(input("Enter the max number:"))

for num in range(1, max_number + 1):
    if num % 2 == 1:
        odd_numbers.append(num)

print("List of odd numbers between 1 and", max_number, ":", odd_numbers)