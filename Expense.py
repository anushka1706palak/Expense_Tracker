import json
from datetime import datetime
import os

# File where data will be saved
FILE_NAME = "data.json"

# Create file if it does not exist
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w") as f:
        json.dump([], f)


def load_expenses():
    """Load expenses from file"""
    with open(FILE_NAME, "r") as f:
        return json.load(f)


def save_expenses(expenses):
    """Save expenses to file"""
    with open(FILE_NAME, "w") as f:
        json.dump(expenses, f, indent=4)


def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping, etc.): ")
    note = input("Enter note (optional): ")

    today = datetime.now().strftime("%Y-%m-%d")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "date": today
    }

    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!\n")


def view_expenses():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses available.\n")
        return

    print("\n---- All Expenses ----")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} ({exp['date']}) | Note: {exp['note']}")
    print()


def monthly_summary():
    expenses = load_expenses()

    if not expenses:
        print("\nNo expenses available.\n")
        return

    totals = {}

    for exp in expenses:
        month = exp["date"][:7]  # Example: 2025-12
        totals[month] = totals.get(month, 0) + exp["amount"]

    print("\n---- Monthly Summary ----")
    for month, total in totals.items():
        print(f"{month}: ₹{total}")
    print()


def main():
    while True:
        print("---- Expense Tracker ----")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. Monthly Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("\nInvalid choice, please try again.\n")


if __name__ == "_main_":
    main()