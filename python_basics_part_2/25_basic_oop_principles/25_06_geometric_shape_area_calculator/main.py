from geometric_shapes import Circle, Rectangle, Triangle

# Creating instances of classes
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Calculating the areas of the shapes
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Outputting the results
print("Circle area:", round(circle_area, 2))
print("Rectangle area:", round(rectangle_area, 2))
print("Triangle area:", round(triangle_area, 2))
