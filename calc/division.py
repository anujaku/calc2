"""This is division calculation that inherits value A and value B from the calculation class"""

from calc.calculation import Calculation

class Division(Calculation):
    """The division class has one method to get the result of the the calculation A and B come from
    the calculation parent class"""
    def get_result(self):
        """method to divide two numbers and return the result"""
        #you need to use self to reference the data contained in the instance of the object.
        #This is encapsulation
        return self.value_a / self.value_b
