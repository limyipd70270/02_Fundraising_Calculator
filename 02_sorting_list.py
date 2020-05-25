


# ***** Functions ******
# Ask user if they want it ordered alphabetically or numerically (price)

expenses_list = " "

# Sorting numerically (cost)
expenses_list.sort(key=lambda x: x[1], reverse=1)

# Output
print("Items ordered by cost <most expensive to least expensive>")
for item in expenses_list:
  print("{}: ${:.2f}".format(item[0], item[1]))

  print()

# Sorting alphabetically
expenses_list.sort(key=lambda x: x[0])

# Output
print("Items in alphabetical order")
for item in expenses_list:
  print("{}: ${:.2f}".format(item[0], item[1]))

# Output the list one line at a time
#

