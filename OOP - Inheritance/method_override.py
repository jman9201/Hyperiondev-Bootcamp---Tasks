""" 
The script takes user inputs for a person's name, age hair colour, and
eye colour. It then determines whether the person is 18 or older. If the
person is 18 or older, it creates an instance of the 'Adult' class;
otherwise, it creates an instance of the 'Child' class.

Finally, it calls the 'can_drive()' method for the respective class
instance to print whether the person is old enough to drive or not

"""

# Define the Adult class
class Adult:
    def __init__(self, name, age, hair_colour, eye_colour):
        self.name = name
        self.age = age
        self.hair_colour = hair_colour
        self.eye_colour = eye_colour
    
    def can_drive(self):
        print(self.name, "is old enough to drive. ")

# Define the Child class as a subclass of Adult
class Child(Adult):
    # Override the can_drive method
    def can_drive(self):
        print(self.name, "is too young to drive. ")

# Take user inputs
name = input("Enter name: ")
age = int(input("Enter age: "))
hair_colour = input("Enter hair colour: ")
eye_colour = input("Enter eye colour: ")

# Logic to determine if the person is 18 or older
if age >= 18:
    person = Adult(name, age, hair_colour, eye_colour)
else:
    person = Child(name, age, hair_colour, eye_colour)

# Call 'can_drive' to print whether the person is old enough to drive
person.can_drive()