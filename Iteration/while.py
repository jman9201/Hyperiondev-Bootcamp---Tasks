# Store sum and count of numbers
total = 0
count = 0

# Continuously ask the the user to enter a number until -1 is entered
while True:
    num = float(input("Enter a number (-1 to stop): "))

    # Check if the enter number is -1
    if num == -1:
        break # Exit the loop if -1 is entered
    else:
        total += num # And the number to the total
        count += 1 # Increment the count of numbers

# Check if at least one number (other than -1) was entered
if count >0:
    # Calculate the average of the numbers (excluding -1)
    average = total / count
    print("Average of the numbers entered:", average)
else:
    print("No Number were entered (except -1).")