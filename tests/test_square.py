import pytest
from shapes.square import Square
from shapes.shape import Shape

def test_square_area():
    square = Square(4)
    assert square.area() == 16, "Square area calculation is incorrect"

def test_square_negative_side():
    with pytest.raises(ValueError, match="Side must be positive"):
        Square(-1)

def test_square_polymorphism():
    shape: Shape = Square(3)
    assert shape.area() == 9, "Polymorphic area calculation failed"