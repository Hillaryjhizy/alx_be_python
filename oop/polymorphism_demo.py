import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")
        # Method to calculate the area of the shape.
        # This method should be overridden by subclasses.
        # Raises:
        #NotImplementedError: if the subclass does not override this method.
        
class Rectangle(Shape):
    def __init__(self, length, width):
        
        self.length = length
        self.width = width
        # Initialize a Rectangle instance with length and width.
        # :param length: float - The length of the rectangle.
        # :param width: float - The width of the rectangle.

    def area(self):
        
        return self.length * self.width
    
        # Calculate the area of the rectangle.
        # Overrides the area method of the Shape base class.
        # :return: float - The area of the rectangle.

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        # Initialize a Circle instance with radius.
        # :param radius: float - The radius of the circle.

    def area(self):
        # Calculate the area of the circle.
        # Overrides the area method of the Shape base class.
        # :return: float - The area of the circle.
        
        return math.pi * (self.radius ** 2)
