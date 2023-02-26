"""
In this example, we have two drawing APIs (DrawingAPI1 and DrawingAPI2) that can draw circles. We also have a Circle class that has a reference to a DrawingAPI object. This allows us to decouple the Circle class from the DrawingAPI implementation. We can then create a Circle object with a specific DrawingAPI object and call its draw method to draw the circle using that API.
"""

from abc import ABC, abstractmethod


class DrawingAPI(ABC):
    @abstractmethod
    def draw_circle(self, x, y, radius):
        pass


class DrawingAPI1(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"Drawing circle with API1 at ({x}, {y}) with radius {radius}.")


class DrawingAPI2(DrawingAPI):
    def draw_circle(self, x, y, radius):
        print(f"Drawing circle with API2 at ({x}, {y}) with radius {radius}.")


class Circle:
    def __init__(self, x, y, radius, drawing_api):
        self._x = x
        self._y = y
        self._radius = radius
        self._drawing_api = drawing_api

    def draw(self):
        self._drawing_api.draw_circle(self._x, self._y, self._radius)

    def scale(self, percent):
        self._radius *= percent


if __name__ == "__main__":
    circle1 = Circle(1, 2, 3, DrawingAPI1())
    circle1.draw()

    circle2 = Circle(4, 5, 6, DrawingAPI2())
    circle2.draw()
