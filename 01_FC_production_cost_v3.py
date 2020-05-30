# Functions

# Number checking function (float for cost, integer for item amounts)
def num_check(question, error_msg, type):
    error = error_msg

    valid = False
    while not valid:
        try:
            response = type(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Ask user for the product they are selling
product = input("What product are you selling to fundraise for?")

# Initialise lists
single_expense= []
total_expenses = []

# Get inputs and add to item_cost list
# Ask for variable items
expense = ""
while expense.lower() != "xxx":

    # list for each row of variable costs
    single_expense = []
    expense = input("Item Name: ")

    # If user enters exit code, break out of loop
    if expense.lower() == "xxx":
        break

    # Ask user how many of each item is needed
    expense_amount = num_check("How many do you need?", "Please enter a whole number more than zero", int)

     # Get the variable item costs
    single_cost = num_check("Item Cost: $", "Please enter a number more than zero", float)

    single_expense.append(expense)
    single_expense.append(single_cost)

    # adds each row of costs to total cost list
    total_expenses.append(single_expense)

# DON'T YOU NEED TO ADD A TOTALLL EXPENSES LIST WITH BOTH SUBLISTS WHICH INCLUDE THE ROWS????

# Ask if they want a fixed_cost list and if so, get inputs for it
fixed_q = input("Do you have any fixed costs?")

if fixed_q == "yes":

print ("{} Fundraiser").format(product)

print ("*** Variable Costs ***")
for item in all_variable_costs:
    print(item)
print()

if fixed_q == "yes":
    print("*** Fixed Costs ***")
    for item in all_fixed_costs:
        print(item)



