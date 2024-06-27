import csv
from datetime import datetime

class ExpenseTracker:
    def __init__(self):
        self.expenses = []
        self.filename = 'expenses.csv'
        self.load_expenses()

    def load_expenses(self):
        try:
            with open(self.filename, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row:
                        self.expenses.append({
                            'date': row[0],
                            'amount': float(row[1]),
                            'category': row[2],
                            'description': row[3]
                        })
        except FileNotFoundError:
            pass

    def save_expenses(self):
        with open(self.filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            for expense in self.expenses:
                writer.writerow([expense['date'], expense['amount'], expense['category'], expense['description']])

    def add_expense(self, amount, category, description):
        date = datetime.now().strftime('%Y-%m-%d')
        self.expenses.append({
            'date': date,
            'amount': amount,
            'category': category,
            'description': description
        })
        self.save_expenses()

    def get_monthly_summary(self):
        monthly_summary = {}
        for expense in self.expenses:
            month = expense['date'][:7]  # Extract YYYY-MM
            if month not in monthly_summary:
                monthly_summary[month] = 0
            monthly_summary[month] += expense['amount']
        return monthly_summary

    def get_category_summary(self):
        category_summary = {}
        for expense in self.expenses:
            category = expense['category']
            if category not in category_summary:
                category_summary[category] = 0
            category_summary[category] += expense['amount']
        return category_summary

    def display_summary(self, summary):
        for key, value in summary.items():
            print(f"{key}: ${value:.2f}")

    def run(self):
        print("Welcome to Expense Tracker!")
        while True:
            print("\n1. Add Expense")
            print("2. View Monthly Summary")
            print("3. View Category Summary")
            print("4. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                try:
                    amount = float(input("Enter amount: "))
                    category = input("Enter category (e.g., food, transportation, entertainment): ")
                    description = input("Enter description: ")
                    self.add_expense(amount, category, description)
                    print("Expense added successfully!")
                except ValueError:
                    print("Invalid input. Please enter the correct values.")
            elif choice == '2':
                monthly_summary = self.get_monthly_summary()
                print("\nMonthly Summary:")
                self.display_summary(monthly_summary)
            elif choice == '3':
                category_summary = self.get_category_summary()
                print("\nCategory Summary:")
                self.display_summary(category_summary)
            elif choice == '4':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    tracker = ExpenseTracker()
    tracker.run()
