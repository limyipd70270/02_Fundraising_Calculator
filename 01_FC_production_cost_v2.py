# Functions

# Number checking function (number must be a float that is more than 0)
def num_check(question, error_msg):
    error = error_msg

    valid = False
    while not valid:
        try:
            response = float(input(question))

            if response <= 0:
                print(error)
            else:
                return response

        except ValueError:
            print(error)


# Ask user for the product they are selling
product = input("What product are you selling to fundraise for?")

# Ask user how much of your product is needed for selling
item_amount = num_check("How much of your product do you need for selling?", "Please enter a whole number more than zero")

# Initialise lists
all_variable_costs = []
all_fixed_costs = []
expenses = []

# Get inputs and add to item_cost list
# Ask for variable items
variable = ""
while variable.lower() != "xxx":

    # list for each row of variable costs
    variable_costs = []
    variable = input("Item Name: ")

    # If user enters exit code, break out of loop
    if variable.lower() == "xxx":
        break

    # Ask user how many of each item is needed
    variable_amount = num_check("How many do you need?", "Please enter a whole number more than zero")

     # Get the variable item costs
    v_cost = float(num_check("Item Cost: $", "Please enter a number more than zero"))

    variable_costs.append(variable)
    variable_costs.append(v_cost)

    # entire variable list
    all_variable_costs.append(variable_costs)

    # Add all_variable_costs to expenses list
    expenses.append(variable_costs)


# Ask if they want a fixed_cost list and if so, get inputs for it
fixed_q = input("Do you have any fixed costs?")

if fixed_q == "yes":
    fixed = ""
    while fixed.lower() != "xxx":
        # list for each row of fixed costs
        fixed_costs = []
        fixed = input("Fixed Cost Name: ")

        # If user enters exit code, break out of loop
        if fixed.lower() == "xxx":
            break

        # Get the fixed item costs
        f_cost = float(num_check("Fixed Cost: $", "Please enter a whole number more than zero"))

        # Add fixed name and cost to cost list
        fixed_costs.append(fixed)
        fixed_costs.append(f_cost)

        # entire variable list
        all_fixed_costs.append(fixed_costs)

        # Add fixed_costs and variable_costs to expenses list
        expenses.append(fixed_costs)

print ("** Variable Costs **")
for item in all_variable_costs:
    print(item)
print()

if fixed_q == "yes":
    print("** Fixed Costs ***")
    for item in all_fixed_costs:
        print(item)

