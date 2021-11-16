""" This is the increment function"""
#first import the addition namespace
from calc.addition import Addition
from calc.division import Division
from calc.subtraction import Subtraction
from calc.multiplication import Multiplication
class Calculator:
    """ This is the Calculator class"""
    #this is the calculator static property
    history = []
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        """method to get result of 1st calculation added to history"""
        return Calculator.history[0].get_result()
    @staticmethod
    def clear_history():
        """Clear history method"""
        Calculator.history.clear()
        return True
    @staticmethod
    def history_count():
        """history_count method"""
        return len(Calculator.history)
    @staticmethod
    def add_calculation_to_history(calculation):
        """Method to add calculation to history"""
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        """method to get last calculation added to history"""
        #-1 gets the last item added to the list automatically &
        # you can expect it to have the get result method
        return Calculator.history[-1].get_result()
    @staticmethod
    def add_number(value_a, value_b):
        """ adds number to result"""
        #create addition object using factory we created on calculation class
        addition = Addition.create(value_a,value_b)
        # addition = Addition(value_a,value_b) <-this is not good but will work.
        # It will be repeated too much
        Calculator.add_calculation_to_history(addition)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    #this is an example of a calling method
    def subtract_number(value_a, value_b):
        """ subtract number from result"""
        #create subtraction object using the factory we created on calculation class
        subtraction = Subtraction.create(value_a, value_b)
        # addition = Addition(value_a,value_b) <-this is not good but will work.
        # It will be repeated too much
        Calculator.add_calculation_to_history(subtraction)
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def multiply_numbers(value_a, value_b):
        """ multiply two numbers and store the result"""
        #this is a shorthand way to create the multiplication object & add it to history in one line
        Calculator.add_calculation_to_history(Multiplication.create(value_a,value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    def divide_numbers(value_a, value_b):
        """divide two numbers and store the result"""
        Calculator.add_calculation_to_history(Division.create(value_a, value_b))
        return Calculator.get_result_of_last_calculation_added_to_history()
