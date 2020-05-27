# ***** Functions ******

expenses_list = " "

# Ask user if they want it ordered alphabetically or numerically (price)
ordering = not_blank ("Would you like it ordered alphabetically (A) or by price (P)?", "Please enter 'A' or 'P'", )
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

