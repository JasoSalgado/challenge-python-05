import math


def square_area(side):
    """Returns the area of a square"""
    return side * side
     

def rectangle_area(base, height):
    """Returns the area of a rectangle"""
    return base * height


def triangle_area(base, height):
    """Returns the area of a triangle"""
    return (base * height)/2


def rhombus_area(diagonal_1, diagonal_2):
    """Returns the area of a rhombus"""
    return diagonal_1 * diagonal_2


def trapezoid_area(base_minor, base_major, height):
    """Returns the area of a trapezoid"""
    return (height * (base_major * base_minor))/2


def regular_polygon_area(perimeter, apothem):
    """Returns the area of a regular polygon"""
    return (perimeter * apothem)/2


def circumference_area(radius):
    """Returns the area of a circumference"""
    return round(math.pi * pow(radius, 2), 1)


if __name__ == '__main__':
    import unittest

    class GeometrySuite(unittest.TestCase):

        def setUp(self):
            self.values = {
                'side':2,
                'base':2,
                'height':5,
                'diagonal_1':6, 
                'diagonal_2':4,
                'base_major':6,
                'perimeter':12,
                'apothem':4,
                'radius':2,
            }


        def test_square_area(self):
            self.assertEqual(4, square_area(self.values['side']))
        

        def test_rectangle_area(self):
            self.assertEqual(10, rectangle_area(self.values['base'],
                                self.values['height']))
        
        
        def test_triangle_area(self):
            self.assertEqual(5, triangle_area(self.values['base'],
                            self.values['height']))


        def test_rhombus_area(self):
            self.assertEqual(24, rhombus_area(self.values['diagonal_1'], 
                            self.values['diagonal_2']))


        def test_trapezoid_area(self):
            self.assertEqual(30, trapezoid_area(self.values['base'], 
                            self.values['base_major'], 
                            self.values['height']))


        def test_regular_polygon_area(self):
            self.assertEqual(24, regular_polygon_area(self.values['perimeter'], 
                            self.values['apothem']))


        def test_circumference_area(self):
            self.assertEqual(12.6, circumference_area(self.values['radius']))


        def tearDown(self):
            del(self.values)


    unittest.main()
