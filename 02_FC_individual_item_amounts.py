# Functions

# Number checking function (number must be a float that is more than 0)
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

# Ask user how many of each item is needed

variable_amount = num_check("How many do you need for selling?", "Please enter a whole number more than zero", int)

