from math import pi

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
