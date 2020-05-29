# ***** Functions ******

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

expenses_list = " "

# Ask user if they want it ordered alphabetically or numerically (price)
ordering = not_blank ("Would you like it ordered alphabetically (A) or by price (P)?", "Please enter 'A' or 'P'", no )
if ordering == "P":
  # Sorting numerically (cost)
  expenses_list.sort(key=lambda x: x[1], reverse=1)

  # Output
  print("Items ordered by cost <most expensive to least expensive>")
  for item in expenses_list:
    print("{}: ${:.2f}".format(item[0], item[1]))



print()

if ordering == "A":
  # Sorting alphabetically
  expenses_list.sort(key=lambda x: x[0])

  # Output
  print("Items in alphabetical order")
  for item in expenses_list:
    print("{}: ${:.2f}".format(item[0], item[1]))

