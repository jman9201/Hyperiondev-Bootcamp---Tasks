### --- OOP Email Simulator --- ###

"""

This program simulates an email application using object-oriented 
programming principles. 

It utilizes an Email class to model emails, featuring attributes such as 
email address, subject line, email content, and a boolean flag indicating 
whether it has been read. 

The application enables users to populate an inbox, view a list of 
emails, mark emails as read, and exit through a menu-driven interface. 

"""

# --- Email Class --- #

class Email:
    # Class variable to store emails
    inbox = []
    
    # Constructor to initialize instance variables
    def __init__(self, email_address, subject_line, email_content):
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False
    
    # Method to mark email as read
    def mark_as_read(self):
        self.has_been_read = True

# --- Lists --- #

# Initialise an empty list to store the email objects.
inbox = []

# --- Functions --- #

# Function to populate inbox with sample emails
def populate_inbox():
    inbox.append(Email("sender1@example.com", 
                       "Welcome to HyperionDev!", 
                       "Dear student, welcome to our platform!"
                       ))
    

    inbox.append(Email("sender2@example.com", 
                       "Great work on the BootCamp!", 
                       "Your progress has been impressive. Keep it up!"
                       ))
    

    inbox.append(Email("sender3@example.com", 
                       "Your excellent marks!", 
                       "Congratulations on achieving top marks in your exams!"
                       ))
    
# Function to list emails in inbox
def list_emails():
    print("Inbox:") # Print header for the list of emails
    for index, email in enumerate(inbox): 
        if email.has_been_read:
            status = "Read"
        else:
            status = "Unread"

        # Print the email index, subject line, and read status
        print(f"{index}. {email.subject_line} - {status}")

# Function to read an email
def read_email(index):
    # Check if the index is within the range of the inbox
    if 0 <= index < len(inbox):
        email = inbox[index]
        print(f"\nEmail from {email.email_address}:")
        print(f"Subject: {email.subject_line}")
        print(f"Content: {email.email_content}")
        email.mark_as_read()

        # Provide feedback to the user
        print("\nEmail marked as read.")
    else:
        # Print error message if index is out of range
        print("Invalid email index.")

# --- Email Program --- #

# Call the function to populate the Inbox for further use in your program
populate_inbox()

# Logic for the various menu operations
menu = True

while True:
    # Prompt user to select an operation from the menu
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))
       
    if user_choice == 1:
        # If user select 1 - prompt for the index and call read_email function
        index = int(input("Enter the index of the email you want to read: "))
        read_email(index)
        
    elif user_choice == 2:
        # If user select 2 - call list_emails function
        list_emails()
            
    elif user_choice == 3:
        # If user select 3, print message and break out of the loop
        print("Exiting application.")
        break

    else:
        # If user input is not valid, print error message
        print("Oops - incorrect input.")
