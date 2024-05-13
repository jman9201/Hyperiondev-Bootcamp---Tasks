# Prompt the user to enter the times (in minutes) for swimming, cycling, and running.
# Read and store the input times for swimming, cycling, and running.
# Calculate the total time taken for the triathlon by adding the individual times.
# Determine the award based on the total time:
#   - If the total time is less than or equal to 100 minutes, award "Provincial colours".
#   - If the total time is between 101 and 105 minutes (inclusive), award "Provincial half colours".
#   - If the total time is between 106 and 110 minutes (inclusive), award "Provincial scroll".
#   - If the total time is more than 110 minutes, award "No award".
# Display the award the participant will receive.

# Prompt the use to enter the times (in minutes)
swim_time = float(input("Enter time taken for swimming (in minutes): "))
cycle_time = float(input("Enter time taken for cycling (in minutes): "))
run_time = float(input("Enter time taken for running (in minutes): "))

# Calculate the total time taken for the triathlon
total_time = swim_time + cycle_time + run_time

if total_time <= 100:
    award = "Provincial colours"
elif 101 <= total_time <= 105:
    award = "Provincial half colours"
elif 106 <= total_time <- 110:
    award = "Provincial scroll"
else:
    award = "No award"

# Display the award the participant will receive
print("The participant will receive the following award based on the total time taken:", award)
