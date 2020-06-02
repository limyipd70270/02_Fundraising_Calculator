# Functions
def not_blank(question, error_msg, num_ok):
    error = error_msg

    valid = False
    while not valid:
        response = input(question)
        has_errors = ""

        if num_ok != "yes":
            # look at each character in string and if it's a number, complain
            for letter in response:
                if letter.isdigit() == True:
                    has_errors = "yes"
                    break

        if response == "":
            print(error)
            continue
        elif has_errors != "":
            print(error)
        else:
            return response

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


# Initialise lists
all_variable_costs = []
expenses = []

# Get inputs and add to variable_costs list
# Ask for variable items
variable = ""
while variable.lower() != "xxx":

    # list for each row of variable costs
    variable_costs = []
    variable = not_blank("Item Name: ", "You can't leave this blank, please enter the item name", "yes")

    # If user enters exit code, break out of loop
    if variable.lower() == "xxx":
        break

    # Ask user how many of each item is needed
    variable_amount = num_check("How many do you need?", "Please enter a whole number more than zero", int)

     # Get the variable item costs
    v_cost = num_check("Item Cost: $", "Please enter a number more than zero", float)

    variable_costs.append(variable)
    variable_costs.append(v_cost)

    # entire variable list
    all_variable_costs.append(variable_costs)


print ("*** Variable Costs ***")
for item in all_variable_costs:
    print(item)
print()


