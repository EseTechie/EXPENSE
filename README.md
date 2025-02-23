# **Altschool first semester project**

**PROJECT DESCRIPTION**

This project is designed to help manage financial expenses using object-oriented programming (OOP) principles in Python. It consists of two main classes: Expense and ExpenseDatabase.

### 1. Expense Class
---
The Expense class represents an individual financial transaction.

Attributes:
1. id: A unique identifier (UUID) assigned automatically.
2. title: A string representing the name of the expense (e.g., "Groceries").
3. amount: A float representing the expense amount.
4. created_at: A timestamp indicating when the expense was created (in UTC).
5. updated_at: A timestamp that updates whenever the expense is modified.
   
Methods: 
__init__(title, amount): Initializes a new expense with a title, amount, and timestamps.
update(title=None, amount=None): Updates the title and/or amount of the expense while also updating the updated_at timestamp.
to_dict(): Returns the expense details as a dictionary.

3. ExpenseDatabase Class
The ExpenseDatabase class is responsible for managing multiple Expense objects.

Attributes:
expenses: A list that stores all Expense instances.
Methods:
__init__(): Initializes an empty list to store expenses.
add_expense(expense): Adds an Expense object to the database.
remove_expense(expense_id): Removes an expense from the database by matching the unique id.
get_expense_by_id(expense_id): Retrieves a specific expense using its unique id.
get_expense_by_title(title): Retrieves a list of expenses that match a given title.
to_dict(): Converts all stored expenses into a list of dictionaries.

**HOW TO CLONE**
To clone the repository, I ran the bash script below 
git clone https://github.com/EseTechie/EXPENSE
cd EXPENSE_MANAGEMENT

**HOW TO RUN THE CODE**
To get a sample output as a demonstration, a Python script was created with the code below;

from expense_manager import Expense, ExpenseDatabase

# Create an instance of ExpenseDatabase
db = ExpenseDatabase()

# Add expenses
expense1 = Expense("Groceries", 50.75)
expense2 = Expense("Transport", 15.20)

db.add_expense(expense1)
db.add_expense(expense2)

# Display all expenses
print("All Expenses:", db.to_dict())

# Retrieve an expense by ID
expense = db.get_expense_by_id(expense1.id)
if expense:
    print("Retrieved Expense by ID:", expense.to_dict())

# Update an expense
expense1.update(amount=55.00)
print("Updated Expense:", expense1.to_dict())

# Remove an expense
db.remove_expense(expense2.id)
print("Expenses after removal:", db.to_dict())


