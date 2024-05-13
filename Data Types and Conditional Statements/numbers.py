# Prompt the user to enter three different integer
# Print the sum all the numbers
# Print the first number minus the second number
# Print the third number multiplied by the first number
# Print the sum all three numbers divided by the third number

num_one =int(input("Enter a number: "))
num_two =int(input("Enter a number: "))
num_three =int(input("Enter a number: "))

num_total = num_one + num_two + num_three
num_min = num_one - num_two
num_multiply = num_three * num_one

print("The sum all the numbers:", num_total)
print("The first number minus the second number:", num_min)
print("The third number multiplied by the first number:", num_multiply)


if num_three != 0:
    print("The sum of all three numbers divided by the third number:", num_one + num_two + num_three / num_three);
else:
    print("Cannot divide by zero. Please ensure the third number is not zero");
