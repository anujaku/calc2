"""This is addition calculation that inherits the value A and value B from the calculation class"""
#this is called a namespace it is like files and folders
#the classes are files and the folders organize the classes
#It looks like a folder and file path
#but it is sort of a virtual representation of how the program is organized

from calc.calculation import Calculation

#This is how you extend the Addition class with the Calculation
class Addition(Calculation):
    """Addition class has one method to get the result of the calculation A and B come from
     calculation parent class"""
    def get_result(self):
        """Method to add two numbers and return the result"""
        #you need to use self to reference the data contained in the instance of the object.
        #This is encapsulation
        return self.value_a + self.value_b
