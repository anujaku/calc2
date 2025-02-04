"""This is our calculation base class / Abstract Class"""
class Calculation:
    """Calculation class has two methods- constructor and create"""

    #contstructor and it is the first function called when an object of the class is instantiated
    def __init__(self,value_a, value_b):
        #self references the instantiated object of the class
        #these are instance properties that are being shared with the child classes
        # (addition, subtraction, etc...)
        self._value_a = value_a
        self._value_b = value_b
    # Class Factory Method <- bound to the class and not the instance of the class

    @classmethod
    def create(cls, value_a, value_b):
        """Using class method to create objects of all individual operations"""
        return cls(value_a,value_b)

    @property
    def value_a(self):
        """Getter For Value A"""
        return self._value_a

    @property
    def value_b(self):
        """Getter For Value B"""
        return self._value_b
