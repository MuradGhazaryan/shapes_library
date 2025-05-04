from math import pi
from .shape import Shape

class Circle(Shape):
    """A class representing a circle."""
    
    def __init__(self, radius: float):
        """
        Initialize a Circle with a given radius.

        Args:
            radius (float): The radius of the circle.

        Raises:
            ValueError: If the radius is negative.
        """
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self) -> float:
        """
        Calculate the area of the circle.

        Returns:
            float: The area of the circle (π * radius^2).
        """
        return pi * self.radius ** 2