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
single_expense= []
expense_list = []

# Get inputs and add to single_expense (each row) list
expense = ""
while expense.lower() != "xxx":

    # list for each row of expenses
    single_expense = []
    expense = not_blank("Item Name: ", "You can't leave this blank, please enter the item name", "yes")

    # If user enters exit code, break out of loop
    if expense.lower() == "xxx":
        break

#How do I separate it for the fixed costs list since it doesn't need an amount for each???

    # Ask user how many of each item is needed
    expense_amount = num_check("How many do you need?", "Please enter a whole number more than zero", int)

     # Get the item costs
    single_cost = num_check("Item Cost: $", "Please enter a number more than zero", float)

    single_expense.append(expense)
    single_expense.append(single_cost)

    # adds each row of costs to cost list
    expense_list.append(single_expense)


for item in expense_list:
    print("{}: {}".format(item[0], item[1]))

