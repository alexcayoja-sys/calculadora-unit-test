import math

class Calculator:
    @staticmethod
    def add(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a + b
    
    @staticmethod
    def subtract(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a - b
    
    @staticmethod
    def multiply(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return a * b
    
    @staticmethod
    def divide(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b
    
    @staticmethod
    def power(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers")
        return math.pow(a, b)
    
    @staticmethod
    def sqrt(a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        if a < 0:
            raise ValueError("Cannot calculate square root of negative numbers")
        return math.sqrt(a)
    
    @staticmethod
    def log10(a):
        if not isinstance(a, (int, float)):
            raise TypeError("Argument must be a number")
        if a <= 0:
            raise ValueError("Logarithm undefined for non-positive numbers")
        return math.log10(a)
