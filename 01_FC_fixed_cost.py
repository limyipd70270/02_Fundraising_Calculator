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
all_fixed_costs = []
expenses = []

# Ask if they want a fixed_cost list and if so, get inputs for it
fixed_q = not_blank("Do you have any fixed costs?", "Please enter 'yes' or 'no'", "yes" )

if fixed_q == "yes":
    fixed = ""
    while fixed.lower() != "xxx":
        # list for each row of fixed costs
        fixed_costs = []
        fixed = not_blank("Fixed Cost Name: ", "You can't leave this blank, please enter what your fixed cost is", "yes")

        # If user enters exit code, break out of loop
        if fixed.lower() == "xxx":
            break

        # Get the fixed item costs
        f_cost = num_check("Fixed Cost: $", "Please enter a whole number more than zero", float)

        # Add fixed name and cost to cost list
        fixed_costs.append(fixed)
        fixed_costs.append(f_cost)

        # entire variable list
        all_fixed_costs.append(fixed_costs)


if fixed_q == "yes":
    print("*** Fixed Costs ***")
    for item in all_fixed_costs:
        print(item)