def check_triangle_type(x, y, z):
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or z == x:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))
print(check_triangle_type(x, y, z))