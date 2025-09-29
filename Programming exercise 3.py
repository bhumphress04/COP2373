from functools import reduce

def main():
    expenses = []

    print("Enter your monthly expenses.")
    print("Type 'done' when you are finished.\n")

    # Collect expenses
    while True:
        expense_type = input("Enter the type of expense (or 'done' to finish): ")
        if expense_type.lower() == 'done':
            break
        try:
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses.append((expense_type, amount))
        except ValueError:
            print("Please enter a valid number for the amount.")

    if not expenses:
        print("No expenses entered.")
        return

    # Use reduce to calculate total
    total = reduce(lambda acc, x: acc + x[1], expenses, 0)

    # Find highest expense
    highest = reduce(lambda a, b: a if a[1] > b[1] else b, expenses)

    # Find lowest expense
    lowest = reduce(lambda a, b: a if a[1] < b[1] else b, expenses)

    # Display results
    print("\nExpense Summary:")
    print(f"Total Expense: ${total:.2f}")
    print(f"Highest Expense: {highest[0]} (${highest[1]:.2f})")
    print(f"Lowest Expense: {lowest[0]} (${lowest[1]:.2f})")

# Run the program
main()
