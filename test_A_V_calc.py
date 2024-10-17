'''
TPRG 2131 Fall 2024 Assignment 1, 
October 16th, 2024
Tomasz Giedrojc
100793058
this is my own work 
'''
# Import the functions from A_V_calc.py
from A_V_calc import rectangle_area, circle_area, cylinder_volume, sphere_volume, triangle_area

# Test the rectangle_area function
def test_rectangle_area():
    assert rectangle_area(3, 4) == 12.0  # 3 * 4 = 12
    assert rectangle_area(5, 5) == 25.0  # 5 * 5 = 25
    assert rectangle_area(2.5, 2.5) == 6.2  # 2.5 * 2.5 = 6.25 (rounded to 6.2)

# Test the circle_area function
def test_circle_area():
    assert circle_area(3) == 28.3  # π * 3² ≈ 28.274333882308138 (rounded to 28.3)
    assert circle_area(5) == 78.5  # π * 5² ≈ 78.53981633974483 (rounded to 78.5)
    assert circle_area(2) == 12.6  # π * 2² ≈ 12.566370614359172 (rounded to 12.6)

# Test the cylinder_volume function
def test_cylinder_volume():
    assert cylinder_volume(3, 5) == 141.4  # π * 3² * 5 ≈ 141.3716694115407 (rounded to 141.4)
    assert cylinder_volume(2, 10) == 125.7  # π * 2² * 10 ≈ 125.66370614359172 (rounded to 125.7)
    assert cylinder_volume(1.5, 4) == 28.3  # π * 1.5² * 4 ≈ 28.274333882308138 (rounded to 28.3)

# Test the sphere_volume function
def test_sphere_volume():
    assert sphere_volume(3) == 113.1  # (4/3) * π * 3³ ≈ 113.09733552923255 (rounded to 113.1)
    assert sphere_volume(5) == 523.6  # (4/3) * π * 5³ ≈ 523.5987755982989 (rounded to 523.6)
    assert sphere_volume(2) == 33.5  # (4/3) * π * 2³ ≈ 33.510321638291124 (rounded to 33.5)

# Test the triangle_area function
def test_triangle_area():
    assert triangle_area(3, 4) == 6.0  # 0.5 * 3 * 4 = 6
    assert triangle_area(5, 10) == 25.0  # 0.5 * 5 * 10 = 25
    assert triangle_area(2.5, 4) == 5.0  # 0.5 * 2.5 * 4 = 5


