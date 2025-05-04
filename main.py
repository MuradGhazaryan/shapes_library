from shapes.circle import Circle
from shapes.triangle import Triangle

def main():
    circle = Circle(5)
    print(f"Circle area: {circle.area()}") 

    triangle = Triangle(3, 4, 5)
    print(f"Triangle area: {triangle.area()}")  
    print(f"Is triangle right-angled? {triangle.is_right_angled()}")  

if __name__ == "__main__":
    main()