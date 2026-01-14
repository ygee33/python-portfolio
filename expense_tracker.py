import csv
import os
import sys
from datetime import datetime

FILE_NAME = 'expenses.csv'

def initialize_file():
    """Check if file exists, create headers if not."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Amount', 'Category', 'Note'])

def add_expense():
    """Prompt user for expense details and save to CSV."""
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid amount. Please enter a number.")
        return

    category = input("Enter category: ").strip()
    note = input("Enter note: ").strip()
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(FILE_NAME, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date, amount, category, note])
    
    print("Expense added successfully!")

def get_expenses():
    """Read expenses from CSV."""
    if not os.path.exists(FILE_NAME):
        return []
    
    expenses = []
    try:
        with open(FILE_NAME, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(row)
    except Exception as e:
        print(f"Error reading file: {e}")
    return expenses

def view_expenses():
    """Display all expenses."""
    expenses = get_expenses()
    if not expenses:
        print("No expenses found.")
        return

    print("\n" + "-"*60)
    print(f"{'Date':<20} | {'Amount':<10} | {'Category':<15} | {'Note'}")
    print("-" * 60)
    for exp in expenses:
        print(f"{exp['Date']:<20} | {float(exp['Amount']):<10.2f} | {exp['Category']:<15} | {exp['Note']}")
    print("-" * 60)

def show_total():
    """Calculate and display total spent."""
    expenses = get_expenses()
    total = sum(float(exp['Amount']) for exp in expenses)
    print(f"\nTotal Spent: ${total:.2f}")

def main():
    initialize_file()
    
    while True:
        print("\n--- Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Show Total Spent")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_expense()
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            show_total()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
