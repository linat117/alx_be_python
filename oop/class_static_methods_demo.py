# class_static_methods_demo.py

class Calculator:
    # Class Attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """Static method: Adds two numbers."""
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """Class method: Multiplies two numbers and shows class-level info."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
