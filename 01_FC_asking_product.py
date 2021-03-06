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


# Ask user for the product they are selling
product = not_blank("What product are you selling to fundraise for? ", "You can't leave this blank, please enter the product you're fundraising for", "yes")

print ("{} Fundraiser".format(product))


