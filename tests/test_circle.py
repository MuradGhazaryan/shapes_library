import pytest
from math import pi
from shapes.circle import Circle
from shapes.shape import Shape

def test_circle_area():
    circle = Circle(5)
    assert abs(circle.area() - pi * 25) < 1e-10, "Circle area calculation is incorrect"

def test_circle_zero_radius():
    circle = Circle(0)
    assert circle.area() == 0, "Circle with zero radius should have zero area"

def test_circle_negative_radius():
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        Circle(-1)

def test_circle_polymorphism():
    shape: Shape = Circle(3)
    assert abs(shape.area() - pi * 9) < 1e-10, "Polymorphic area calculation failed"