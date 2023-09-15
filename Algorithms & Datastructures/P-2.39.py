my_name = "Tyler Zenisek"

from abc import ABC, abstractmethod
import math


class Polygon(ABC):
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

# YOUR CODE HERE

class RightTriangle(Polygon):
    def area(self):
        return .5 * self._height * self._width

    def perimeter(self):
        a = pow(self._width,2)
        b = pow(self._height,2)
        c = a + b

        return math.sqrt(c) + self._width + self._height


# YOUR CODE HERE

class Rectangle(Polygon):
    def area(self):
        return self._width * self._height

    def perimeter(self):
        return (2 * self._width) + (2 * self._height)

# YOUR CODE HERE

class Square(Rectangle):  # A square is a specific type of rectangle
    def __init__(self, dim):
        self._width = dim
        self._height = dim

# YOUR CODE HERE


if __name__ == "__main__":
    # create a right triangle with base 3 and height 4
    rt = RightTriangle(3, 4)
    print("Right Triangle area:", rt.area())
    print("Right Triangle perimeter:", rt.perimeter())

    # create a rectangle with width 3 and height 4
    rect = Rectangle(3, 4)
    print("Rectangle area:", rect.area())
    print("Rectangle perimeter:", rect.perimeter())

    # create a square with side 3
    sq = Square(3)
    print("Square area:", sq.area())
    print("Square perimeter:", sq.perimeter())
