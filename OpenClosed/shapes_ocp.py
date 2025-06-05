from math import pi
from abc import ABC, abstractmethod

class Shape:
    def __init__(self, shape_type, **kwargs):
        self.shape_type = shape_type
        if self.shape_type == "rectangle":
            self.width = kwargs["width"]
            self.length = kwargs["length"]
        elif self.shape_type == "circle":
            self.radius = kwargs["radius"]
        
    def calculate_area(self):
        if self.shape_type == "rectangle":
            return self.width * self.length
        elif self.shape_type == "circle":
            return pi * (self.radius ** 2)
    
    def perimeter(self):
        if self.shape_type == "rectangle":
            return 2 * (self.length * self.width)
        elif self.shape_type == "circle":
            return 2 * pi * self.radius

class Shape(ABC):
    def __init__(self, shape_type):
        self.shape_type == shape_type

    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        super().__init__("circle")
        self.radius = radius

    def calculate_area(self):
        return pi * (self.radius ** 2)
    
    def perimeter(self):
        return 2 * pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__("rectangle")
        self.width = width
        self.height = height
   
    def calculate_ares(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Square(Shape):
    def __init__(self, side):
        super().__init__("square")
        self.side = side
    
    def calculate_area(self):
        return self.side * self.side
    
    def perimeter(self):
        return 4 * self.side