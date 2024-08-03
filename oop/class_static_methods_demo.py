class Calculator:
    # Class attribute that holds a value related to the calculation type
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        
        #A method to add two numbers. Static methods do not have access to the class or instance itself.
        #They are utility methods that perform a task in isolation.
        # :param a: int - First number to add.
        # :param b: int - Second number to add.
        # :return: int - Sum of the two numbers.
        
        return a + b

    @classmethod
    def multiply(cls, a, b):
        
        # A Class method to multiply two numbers. This Class methods have access to the class via the 'cls' parameter. 
        # They can modify class state that applies across all instances.
        # :param a: int - First number to multiply.
        # :param b: int - Second number to multiply.
        # :return: int - Product of the two numbers.
        
        # Print the class attribute 'calculation_type'
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
