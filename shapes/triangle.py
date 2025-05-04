from .shape import Shape

class Triangle(Shape):
    """A class representing a triangle."""

    def __init__(self, a: float, b: float, c: float):
        """
        Initialize a Triangle with three sides.

        Args:
            a (float): Length of the first side.
            b (float): Length of the second side.
            c (float): Length of the third side.

        Raises:
            ValueError: If any side is not positive or if the sides cannot form a triangle.
        """
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Sides must be positive")
        if a + b <= c or b + c <= a or a + c <= b:
            raise ValueError("Invalid triangle sides")
        self.a = a
        self.b = b
        self.c = c

    def area(self) -> float:
        """
        Calculate the area of the triangle using Heron's formula.

        Returns:
            float: The area of the triangle.
        """
        s = (self.a + self.b + self.c) / 2  
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def is_right_angled(self) -> bool:
        """
        Check if the triangle is right-angled.

        Returns:
            bool: True if the triangle is right-angled, False otherwise.
        """
        sides = sorted([self.a, self.b, self.c])
        return abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-10