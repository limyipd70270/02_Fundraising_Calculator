# Initialise lists
single_expense= [['rent', 50.0], ['adds', 2.0]]
expense_list = [['mugs', 1.0], ['printing', 2.0]]

# get subtotal

single_subtotal = 0
for item in single_expense:
    single_subtotal += item[1]

print("Subtotal: ${:.2f}".format(single_subtotal))

