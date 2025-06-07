from abc import ABC, abstractmethod

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def calculate_area(self)-> float:
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side: float):
        super().__init__(side, side)

    def __setattr__(self, key, value):
        super().__setattr__(key, value)
        if key in ("width", "height"):
            self.__dict__["width"] = value
            self.__dict__["heigth"] = value


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height
    
    def calculate_area(self)-> float:
        return self.width * self.height
    
    def perimeter(self)-> float:
        return 2 * (self.width + self.height)

class Square(Shape):
    def __init__(self, side: float):
        self.side = side
    
    def calculate_area(self)-> float:
        return self.side * self.side

    def perimeter(self)-> float:
        return 4 * self.side