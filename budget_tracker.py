# Dynamic Budget Tracker

# Ask for total monthly budget
try:
    budget = float(input("Enter your total monthly budget (in LKR): "))
    expenses = []

    # Loop to enter expenses
    while True:
        expense_input = input("Enter an expense amount (or type 'done' to finish): ").strip().lower()
        if expense_input == 'done':
            break
        try:
            expense = float(expense_input)
            if expense < 0:
                print("Expense cannot be negative. Please enter a positive amount.")
                continue
            expenses.append(expense)
        except ValueError:
            print("Invalid input. Please enter a numeric value or 'done'.")

    # Calculate total expenses and remaining balance
    total_expenses = sum(expenses)
    remaining_balance = budget - total_expenses

    # Display results
    print("\n" + "="*40)
    print("BUDGET TRACKER SUMMARY")
    print("="*40)
    print(f"Total Monthly Budget: {budget:.2f} LKR")
    print(f"Total Expenses: {total_expenses:.2f} LKR")
    print(f"Remaining Balance: {remaining_balance:.2f} LKR")
    print("="*40)

    # Check for low funds warning
    if remaining_balance < 500:
        print("Warning: Low Funds")

except ValueError:
    print("Invalid budget amount. Please enter a numeric value.")
    input("\nPress Enter to exit...")

