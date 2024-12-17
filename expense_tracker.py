import os
import datetime

FILE_NAME = "expenses.txt"

def display_menu():
    print("\nWelcome to the Expense Tracker!")
    print("1. Add an expense")
    print("2. View all expenses")
    print("3. Search expenses by date")
    print("4. Calculate total spending")
    print("5. Exit")

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    category = input("Enter category: ").strip()
    description = input("Enter description: ").strip()
    try:
        amount = float(input("Enter amount: ").strip())
    except ValueError:
        print("Amount must be a number.")
        return

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{description},{amount:.2f}\n")
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    print("\n--- All Expenses ---")
    print(f"{'Date':<12} | {'Category':<10} | {'Description':<20} | {'Amount':>8}")
    print("-" * 55)
    with open(FILE_NAME, "r") as file:
        for line in file:
            date, category, description, amount = line.strip().split(",")
            print(f"{date:<12} | {category:<10} | {description:<20} | ${float(amount):>7.2f}")

def search_expenses_by_date():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    date = input("Enter date to search (YYYY-MM-DD): ").strip()
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")  # Validate date format
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    print("\n--- Expenses for", date, "---")
    print(f"{'Category':<10} | {'Description':<20} | {'Amount':>8}")
    print("-" * 40)
    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            record_date, category, description, amount = line.strip().split(",")
            if record_date == date:
                found = True
                print(f"{category:<10} | {description:<20} | ${float(amount):>7.2f}")
    if not found:
        print("No expenses found for the given date.")

def calculate_total_spending():
    if not os.path.exists(FILE_NAME):
        print("No expenses recorded yet.")
        return

    total = 0
    with open(FILE_NAME, "r") as file:
        for line in file:
            _, _, _, amount = line.strip().split(",")
            total += float(amount)
    print(f"Total Spending: ${total:.2f}")


while True:
    display_menu()
    choice = input("Choose an option: ").strip()
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        search_expenses_by_date()
    elif choice == "4":
        calculate_total_spending()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")