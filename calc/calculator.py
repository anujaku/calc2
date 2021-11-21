""" This is the increment function"""
from calc.calculations.addition import Addition
from calc.calculations.subtraction import Subtraction
from calc.calculations.multiplication import Multiplication
from calc.calculations.division import Division

class Calculator:
    """ This is the Calculator class"""
    history = []
    @staticmethod
    def add_numbers(*args):
        """ adds list of numbers"""
        calculation = Addition(args)
        Calculator.history.append(calculation)
        return calculation.get_result()
    @staticmethod
    def clear_history():
        """ Clear the calculation history"""
        Calculator.history.clear()
        return True
    @staticmethod
    def get_calculation(num):
        """ get a specific calculation from history"""
        return Calculator.history[num]
    @staticmethod
    def get_calculation_last():
        """ get last calculation from history"""
        return Calculator.history[-1]
    @staticmethod
    def subtract_numbers(*args):
        """ subtract a list of numbers from result"""
        calculation = Subtraction(args)
        Calculator.history.append(calculation)
        return calculation.get_result()
    @staticmethod
    def multiply_numbers(*args):
        """ multiplication number from result"""
        calculation = Multiplication(args)
        return calculation.get_result()
    @staticmethod
    def divide_numbers(*args):
        """ multiplication number from result"""
        division = Division(args)
        return division.get_result()
