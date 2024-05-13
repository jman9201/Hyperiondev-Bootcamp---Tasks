# Ask the user how many students are registering and store the value
# Open a text file named "reg_form.txt" in "w" mode to store the IDs
# Start a for loop that runs for the number of students entered by the users
# Inside the loop:
#   - Ask the user to enter the ID for the current student
#   - Write the student ID to the file
#   - Write a dotted line as a separator after each student ID
# After the loop, close the file
# Print a message indicating that the registration IDs have been saved

# Ask the user how many students are registering
num_students = int(input("How many students are registering? "))

# Open a text file in append mode to store the registration IDs
with open("reg_form.txt", "w") as file: 
    for i in range(num_students):

        # Ask the user to enter the student ID
        student_id = input(f"\nEnter ID for student {i+1}: ")
        
        # Write the student ID to the file
        file.write(student_id + "\n")
        
        # Write a dotted line as a separator after each student ID
        file.write("-" * 20 + "\n")
        print(f"Student {i+1} registered successfully.")

# Print a message to indicate the registration IDs have been saved
print("\nStudent registration IDs have been saved to reg_form.txt")