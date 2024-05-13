"""

This code defines a base class 'Course' with attributes 'name' and 
'contact_website', along with a method 'contact_details' to display 
contact information. 

The task entails extending this class by adding a new method to print 
the head office location, creating a subclass named 'OOPCourse', and 
defining its constructor to initialize specific attributes with default 
values. 

Two additional methods, 'trainer_details' and 'show_course_id', are 
implemented in the subclass. 

Finally, an instance of 'OOPCourse' is created and its methods are 
invoked to print relevant details.

"""

class Course:
    name = "Fundamentals of Computer Science"
    contact_website = "www.hyperiondev.com"
    head_office_location = "Cape Town"

    def contact_details(self):
        #Prints contact details and head office location
        print("Please contact us by visiting", self.contact_website)
        print("Head Office Location:", self.head_office_location)

class OOPCourse(Course):
    def __init__(self, 
                 description="OOP Fundamentals", 
                 trainer="Mr Anon A.mouse"
                 ):
        
        #Initializes OOPCourse instance with description and trainer
        self.description = description
        self.trainer = trainer

    def trainer_details(self):
        #Prints course description and trainer
        print("This course is about", self.description)
        print("Trainer:", self.trainer)
    
    def show_course_id(self):
        #Prints the ID number of the course
        print("ID number of the course: #12345")

# Create an instance of OOPCourse and call its methods
course_1 = OOPCourse()

# Print contact and head office, description with trainer, and course ID
course_1.contact_details()
course_1.trainer_details()
course_1.show_course_id()