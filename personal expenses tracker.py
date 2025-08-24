import json
from datetime import datetime

# ....to store all expenses we use a list.....
expenses = []


# ---- Data Load Function ----
def load_data():
    global expenses
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except FileNotFoundError:
        expenses = []


# ---- Data Save Function ----
def save_data():
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)


# ---- Add Expense ----
def add_expense(amount, category):
    expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d")
    }
    expenses.append(expense)
    save_data()
    print("Expense added successfully!")


# ---- View Summary ----
def view_summary():
    if not expenses:
        print(" No expenses found.")
        return

    total = 0
    category_summary = {}

    for e in expenses:
        total += e["amount"]
        if e["category"] in category_summary:
            category_summary[e["category"]] += e["amount"]
        else:
            category_summary[e["category"]] = e["amount"]

    print("\n Expense Summary:")
    print(f"Total Spending: ₹{total}")
    for cat, amt in category_summary.items():
        print(f"{cat}: ₹{amt}")


# ---- Main Program ----
def main():
    load_data()
    while True:
        print("--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")
        choice = input("Enter choice: ")



        if choice == "1":
            try:
                amount = float(input("Enter amount: ₹"))
                category = input("Enter category (Food/Travel/etc): ")
                add_expense(amount, category)
            except ValueError:
                print(" Please enter a valid number for amount.")
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Exiting... Data saved.")
            break
        else:
            print(" Invalid choice, try again.")

# Run program
main()
