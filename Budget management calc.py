# Simple Budget Tracker

print("=== Budget Tracker ===\n")

# Step 1: Ask for the total budget
while True:
    try:
        budget = float(input("Enter your total budget: $"))
        if budget > 0
            break  # valid budget, exit loop
        else:
            print("Please enter a number greater than 0.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Step 2: Track expenses
expenses = []  # empty list to store expenses

while True:
    entry = input("Enter an expense amount (or type 'done' to finish): ")

    if entry.lower() == "done":  # stop when user is finished
        break

    try:
        expense = float(entry)
        if expense >= 0:  # prevent negative expenses
            expenses.append(expense)  # add to the list
        else:
            print("Expense cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# Step 3: Calculate total spent and balance
total_spent = sum(expenses)
remaining = budget - total_spent

# Step 4: Show results
print("\n----- Results -----")
print(f"Total Budget: ${budget:.2f}")
print(f"Total Spent: ${total_spent:.2f}")
print(f"Remaining Balance: ${remaining:.2f}")

# Step 5: Check if the user went over budget
if remaining < 0:
    print(" You are OVER budget!")
else:
    print("You are within budget.")
