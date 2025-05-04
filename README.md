# Shapes Library
A Python library for calculating the area of geometric shapes, designed for external clients.

## Features
- Calculate the area of a circle by radius.
- Calculate the area of a triangle by three sides using Heron's formula.
- Check if a triangle is right-angled using the Pythagorean theorem.
- Extensible architecture for adding new shapes (e.g., Square).
- Comprehensive unit tests using pytest.
- Polymorphic area calculation without knowing the shape type at compile-time.

## Installation
1. Clone the repository or download the source code.
2. Navigate to the project directory.
3. Install dependencies:

```bash
pip install pytest
```

## Usage
```python
from shapes.circle import Circle
from shapes.triangle import Triangle
from shapes.square import Square

# Circle
circle = Circle(5)
print(f"Circle area: {circle.area()}")  # Output: ~78.5398

# Triangle
triangle = Triangle(3, 4, 5)
print(f"Triangle area: {triangle.area()}")  # Output: 6.0
print(f"Is right-angled? {triangle.is_right_angled()}")  # Output: True

# Square
square = Square(4)
print(f"Square area: {square.area()}")  # Output: 16.0

# Polymorphic usage
shapes = [Circle(3), Triangle(3, 4, 5), Square(2)]
for shape in shapes:
    print(f"Area: {shape.area()}")  # Output: ~28.2743, 6.0, 4.0
```

## Running Tests
1. Navigate to the project directory.
2. Run:
```bash
pytest -v
```
This will execute all unit tests for Circle, Triangle, and Square.

## Adding New Shapes
To add a new shape:

1. Create a new class in the shapes directory that inherits from Shape.
2. Implement the area method.
3. Add unit tests in the tests directory.
4. Example: See square.py and test_square.py.

## Project Structure
```
shapes_library/
├── shapes/
│   ├── __init__.py
│   ├── shape.py
│   ├── circle.py
│   ├── triangle.py
│   ├── square.py
├── tests/
│   ├── __init__.py
│   ├── test_circle.py
│   ├── test_triangle.py
│   ├── test_square.py
├── README.md
├── requirements.txt
```

## Requirements
- Python 3.6+
- pytest (for running tests)

## License
MIT License