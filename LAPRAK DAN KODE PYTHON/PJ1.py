def triangle_type(x: int, y: int, z: int) -> str:
    """
    Determine the type of triangle based on the lengths of its sides.

    Args:
    x (int): Length of the first side of the triangle.
    y (int): Length of the second side of the triangle.
    z (int): Length of the third side of the triangle.

    Returns:
    str: Type of triangle ('Equilateral', 'Isosceles', or 'Scalene').
    """
    # Check if it forms a valid triangle
    if x + y <= z or x + z <= y or y + z <= x:
        return "Not a triangle"
    elif x == y == z:
        return "Equilateral triangle"  # Sides are equal
    elif x == y or x == z or y == z:
        return "Isosceles triangle"  # Two sides are equal
    else:
        return "Scalene triangle"  # No sides are equal

# Example usage:
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

print(triangle_type(side1, side2, side3))


