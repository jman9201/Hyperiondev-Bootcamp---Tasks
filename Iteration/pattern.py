# Define the number of rows
num_rows = 9

# Iterate through each row
for i in range(1, num_rows + 1):
    # Check if we are in the first half of rows or the second half
    if i <= (num_rows + 1) // 2:
        # Print increasing number of asterisks for the first half of rows
        print('*' * i)
    else:
        # Print decreasing number of asterisks for the second half of rows
        print('*' * (num_rows - i + 1))