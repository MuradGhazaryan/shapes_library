import pytest
from shapes.triangle import Triangle
from shapes.shape import Shape

def test_triangle_area():
    triangle = Triangle(3, 4, 5)
    assert abs(triangle.area() - 6) < 1e-10, "Triangle area calculation is incorrect"

def test_right_angled_triangle():
    triangle = Triangle(3, 4, 5)
    assert triangle.is_right_angled(), "Triangle (3,4,5) should be right-angled"

def test_non_right_angled_triangle():
    triangle = Triangle(2, 3, 4)
    assert not triangle.is_right_angled(), "Triangle (2,3,4) should not be right-angled"

def test_negative_side():
    with pytest.raises(ValueError, match="Sides must be positive"):
        Triangle(-1, 2, 2)

def test_invalid_triangle():
    with pytest.raises(ValueError, match="Invalid triangle sides"):
        Triangle(1, 1, 3)

def test_triangle_polymorphism():
    shape: Shape = Triangle(3, 4, 5)
    assert abs(shape.area() - 6) < 1e-10, "Polymorphic area calculation failed"