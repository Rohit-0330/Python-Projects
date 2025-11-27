import json
from datetime import datetime

FILE = "data.json"

def load_data():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_expense():
    title = input("Expense Title: ")
    amount = float(input("Amount: "))
    date = datetime.now().strftime("%Y-%m-%d %H:%M")

    data = load_data()
    data.append({"title": title, "amount": amount, "date": date})
    save_data(data)
    print("Expense added!")

def view_expenses():
    data = load_data()
    for exp in data:
        print(f"{exp['date']} - {exp['title']} - ₹{exp['amount']}")

def menu():
    while True:
        print("\n1. Add Expense\n2. View Expenses\n3. Exit")
        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        else:
            break

if __name__ == "__main__":
    menu()
