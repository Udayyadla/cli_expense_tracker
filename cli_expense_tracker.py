import json
import os

FILE_NAME = "expenses.json"


def load_expenses():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_expenses(expenses):
    with open(FILE_NAME, "w") as file:
        json.dump(expenses, file, indent=4)


def is_duplicate_expense(expenses, expense):
    for existing_expense in expenses:
        if (
            existing_expense["name"].lower() == expense["name"].lower()
            and existing_expense["amount"] == expense["amount"]
            and existing_expense["category"] == expense["category"]
        ):
            return True
    return False


def add_expense(expenses):
    expense_name = input("Enter the expense name: ").strip()
    if not expense_name:
        print("Expense name cannot be empty.")
        return

    try:
        expense_amount = float(input("Enter the expense amount: "))
        if expense_amount <= 0:
            print("Expense amount must be greater than 0.")
            return
    except ValueError:
        print("Invalid expense amount. Please enter a valid number.")
        return

    expense_category = input("Enter the expense category: ").strip()
    if not expense_category:
        print("Expense category cannot be empty.")
        return

    expense = {
        "name": expense_name,
        "amount": expense_amount,
        "category": expense_category,
    }
    if is_duplicate_expense(expenses, expense):
        print("Expense already exists.")
        return
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully.")


def show_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(
            f"{index}. {expense["name"]} - {expense["amount"]} - {expense["category"]}"
        )
    return


def delete_expense(expenses, expense_id):
    if expense_id < 1 or expense_id > len(expenses):
        print("Invalid expense ID.")
        return
    deleted_expense = expenses.pop(expense_id - 1)
    save_expenses(expenses)
    print(
        f"Expense {deleted_expense["name"]} - {deleted_expense["amount"]} - {deleted_expense["category"]} deleted successfully."
    )
    return


def total_expenses(expenses):
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total expenses: {total}")
    return


def filter_expenses_by_category(expenses, category):
    filtered_expenses = []
    for expense in expenses:
        if expense["category"].lower().strip() == category.lower().strip():
            filtered_expenses.append(expense)
    if not filtered_expenses:
        print(f"No expenses found for the {category} category.")
        return
    for expense in filtered_expenses:
        print(f"{expense["name"]} | {expense["amount"]} | {expense["category"]}")
    return


def main():

    expenses = load_expenses()
    while True:
        print("--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. Show Expenses")
        print("3. Delete Expense")
        print("4. Total Expenses")
        print("5. Filter Expenses by Category")
        print("6. Exit")
        try: 
           choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            conti

        if choice == 1:
            add_expense(expenses)

        elif choice == 2:
            show_expenses(expenses)
        elif choice == 3:
            expense_id = int(input("Enter the expense Id to delete : "))
            delete_expense(expenses, expense_id)
        elif choice == 4:
            total_expenses(expenses)
        elif choice == 5:
            category = input("Enter the category to filter:")
            filter_expenses_by_category(expenses, category)
        elif choice == 6:
            print("Goodbye!")
            return
        else:
            print("Invalid Choice. Please choose a valid option.")


main()
