import math


def calculate_area_rectangle():
# rectangle
    width = input('Enter the width of the rectangle: ')
    height = input('Enter the height of the rectangle: ')
    area = float(width) * float(height)
    return area

# circle
def calculate_area_circle():
    radius = input('Enter the radius of the circle: ')
    area_of_circle = float(math.pi * float(radius)**2)
    return area_of_circle

#triangle
def calculate_area_triangle():
    tri_base = input('Enter the base of the triangle: ')
    tri_height = input('Enter the height of the triangle: ')
    tri_area = float(tri_base) * float(tri_height) / 2
    return tri_area

def calculate_square_perimeter(side_length):
    perimeter = int(side_length) * 4
    area = side_length * side_length
    return perimeter, area


def circumference(radius):
    circumference = 2 * math.pi * float(radius)
    area_of_circle = math.pi * float(radius)**2
    return circumference, area_of_circle


def geometry(side_length_square, radius_circle):
    perimeter = calculate_square_perimeter(side_length_square)
    radius_square = circumference(radius_circle)

    if perimeter[0] > radius_square[0]:
        print(f'Square has a larger perimeter')
    elif perimeter[0] < radius_square[0]:
        print(f'Circle has a larger circumference')
    if perimeter[1] > circumference(radius_square)[1]:
        print(f'Square has a larger area')
    elif perimeter[1] < circumference(radius_square)[1]:
        print(f'Circle has a larger area')


print(geometry(9,3))

