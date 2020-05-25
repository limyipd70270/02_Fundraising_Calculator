# Ask user for the product they are selling
product = input("What product are you selling to fundraise for?")

# Ask user how many items are needed for selling !!! DO FOR EACH ITEM
item_amount = input("How many items do you need for selling?")

# Initialise lists
variable_costs = []
fixed_costs = []
item_costs = []
expenses = []

# Get inputs and add to item_cost list
# Ask for variable items
variable = ""
while variable.lower() != "xxx":
    variable = input("Item Name: ")

    # If user enters exit code, break out of loop
    if variable.lower() == "xxx":
        break

     # Get the variable item costs
    v_cost = float(input("Item Cost: $"))

# Ask if they want a fixed_cost list and if so, get inputs for it
fixed_q = input ("Do you have any fixed costs?")
yes = ["y, yes"]

if fixed_q in yes:
    while fixed.lower() != "xxx":
        fixed = input("Item Name: ")

        # If user enters exit code, break out of loop
        if fixed.lower() == "xxx":
            break

            # Get the fixed item costs
        f_cost = float(input("Item Cost: $"))

        # Add fixed name and cost to cost list
        variable_costs.append(variable)
        variable_costs.append(v_cost)

        # Add fixed_costs and variable_costs to expenses list
        expenses.append(variable_costs, fixed_costs)
else:
    # Add variable name and cost to cost list
    variable_costs.append(variable)
    variable_costs.append(v_cost)

    # Add variable_costs to expenses list
    expenses.append(variable_costs)

print (expenses)

print (("{} fundraiser").format(product))

