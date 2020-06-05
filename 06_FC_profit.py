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


# Number checking function
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


# Ask if their profit will be in $ or %)
profit = ""
profit_type = not_blank("Is your profit in '$' or '%'?", "Please enter '$' or '%'", "no")

if profit_type == "$":
    # Get profit in $__
    profit = num_check("How much profit would you like to make? $", "Please enter a number more than zero", float)
    print("${}".format(profit))

if profit_type == "%":
    # Get profit in %__
    profit = num_check("How much profit would you like to make? %", "Please enter a number more than zero", float)
    print("%{}".format(profit))

