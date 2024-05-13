import unittest
from method_override import Adult, Child

class TestDrivingEligibility(unittest.TestCase):
    
    def test_adult_can_drive(self):
        # Arrange
        adult = Adult("John", 25, "Brown", "Blue")
        
        # Act
        result = adult.can_drive()
        
        # Assert
        self.assertEqual(result, "John is old enough to drive. ")
    
    def test_child_cannot_drive(self):
        # Arrange
        child = Child("Alice", 12, "Blonde", "Green")
        
        # Act
        result = child.can_drive()
        
        # Assert
        self.assertEqual(result, "Alice is too young to drive. ")
    
    def test_person_instance_creation(self):
        # Arrange
        adult_person = Adult("Mike", 20, "Black", "Brown")
        child_person = Child("Sara", 10, "Red", "Blue")
        
        # Act
        adult_instance = isinstance(adult_person, Adult)
        child_instance = isinstance(child_person, Child)
        
        # Assert
        self.assertTrue(adult_instance)
        self.assertTrue(child_instance)
        

if __name__ == '__main__':
    unittest.main()