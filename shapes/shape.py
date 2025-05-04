from abc import ABC, abstractmethod

class Shape(ABC):
    """Abstract base class for geometric shapes."""

    @abstractmethod
    def area(self) -> float:
        """
        Calculate the area of the shape.

        Returns:
            float: The area of the shape.
        """
        pass