from .shape import Shape

class Square(Shape):
    """A class representing a square."""

    def __init__(self, side: float):
        """
        Initialize a Square with a given side length.

        Args:
            side (float): The length of the square's side.

        Raises:
            ValueError: If the side is not positive.
        """
        if side <= 0:
            raise ValueError("Side must be positive")
        self.side = side

    def area(self) -> float:
        """
        Calculate the area of the square.

        Returns:
            float: The area of the square (side^2).
        """
        return self.side ** 2