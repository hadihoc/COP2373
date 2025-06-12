# This program asks the user for a list of their monthly expenses, then displays
# the total, the highest and lowest expenses

from functools import reduce


def get_expenses(expenses):
    while True:
        try:
            expense_type = input("Enter the name of the expense (or type e to finish): ")

            if expense_type.lower() == 'e':
                break
            amount = float(input(f"Enter the amount for {expense_type}: "))
            expenses[expense_type] = amount
        except ValueError:
            print("Please enter a valid number for the amount.")

    return expenses


def main():
    # Creating an empty dictionary and named expenses
    expenses = {}

    # Get expenses by Calling get_expenses function
    expenses = get_expenses(expenses)

    # Calculating the total expenses in the expenses dict
    total_expenses = sum(expenses.values())

    # Sorting the expenses dict by values in ascending order
    # and assigned to a new dict named sorted_expenses
    sorted_expenses = dict(sorted(expenses.items(), key=lambda item: item[1]))

    # Getting the lowest expense
    min_type, min_value = next(iter(sorted_expenses.items()))

    # Getting the highest expense
    max_type, max_value = next(reversed(sorted_expenses.items()))

    print()
    print(f"The total of all expenses are: ${total_expenses}.")
    print()
    print(f"The lowest expense is ${min_value} for {min_type}")
    print()
    print(f"The highest expense is ${max_value} for {max_type}")


if __name__ == "__main__":
    main()

