#!/usr/bin/python3
"""
Unittest for Square Class
"""
import unittest
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    unittests for functions in Square Class
    """

    def test_ints(self):
        s1 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.width, 5)
        self.assertEqual(s1.height, 5)

        s2 = Square(6, 5)
        self.assertEqual(s2.width, 6)
        self.assertEqual(s2.height, 6)
        self.assertEqual(s2.x, 5)

        s3 = Square(1, 2, 3, 4)
        self.assertEqual(s3.width, 1)
        self.assertEqual(s3.height, 1)
        self.assertEqual(s3.x, 2)
        self.assertEqual(s3.y, 3)
        self.assertEqual(s3.id, 4)

    def test_arg_type(self):
        with self.assertRaises(TypeError):
            Square("1", 2, 3, 4)
        with self.assertRaises(TypeError):
            Square(1, [2], 3, 4)
        with self.assertRaises(TypeError):
            Square(1, {2}, 3, 4)
        with self.assertRaises(TypeError):
            Square((1, 2), 3, 4)
        with self.assertRaises(TypeError):
            Square(1, 2, {"k": 3}, 4)
        with self.assertRaises(TypeError):
            Square(1, "Holberton", 3, 4)

    def test_arg_value(self):
        with self.assertRaises(ValueError):
            Square(0, 2, 3, 4)
        with self.assertRaises(ValueError):
            Square(0, 0, 0, 4)
        with self.assertRaises(ValueError):
            Square(1, -2, 3, 4)
        with self.assertRaises(ValueError):
            Square(-1, 2, -3, 4)

    def test_area(self):
        s4 = Square(3)
        self.assertEqual(s4.area(), 9)

        s5 = Square(2, 10)
        self.assertEqual(s5.area(), 4)

        s6 = Square(8, 7, 0, 1)
        self.assertEqual(s6.area(), 64)

    def test_str_format(self):
        s7 = Square(1, 2, 3, 4)
        self.assertEqual(s7.__str__(), "[Square] (4) 2/3 - 1")

    def test_update_args(self):
        s8 = Square(1, 2, 3, 4)
        s8.update(89)
        self.assertEqual(s8.__str__(), "[Square] (89) 2/3 - 1")

        s8.update(89, 12)
        self.assertEqual(s8.__str__(), "[Square] (89) 2/3 - 12")

        s8.update(89, 12, 13)
        self.assertEqual(s8.__str__(), "[Square] (89) 13/3 - 12")

        s8.update(89, 12, 13, 14)
        self.assertEqual(s8.__str__(), "[Square] (89) 13/14 - 12")

    def test_update_kwargs(self):
        s9 = Square(1, 2, 3, 4)
        s9.update(id=10)
        self.assertEqual(s9.__str__(), "[Square] (10) 2/3 - 1")

        s9.update(id=10, size=20)
        self.assertEqual(s9.__str__(), "[Square] (10) 2/3 - 20")

        s9.update(id=10, size=20, x=30)
        self.assertEqual(s9.__str__(), "[Square] (10) 30/3 - 20")

        s9.update(id=10, size=20, x=30,  y=50)
        self.assertEqual(s9.__str__(), "[Square] (10) 30/50 - 20")

    def test_to_dictionary(self):
        s10 = Square(1, 2, 3, 4)
        representation = {'id': 4, 'x': 2, 'size': 1, 'y': 3}
        self.assertEqual(s10.to_dictionary(), representation)

    def test_create(self):
        s11 = Square.create(**{'id': 1, 'size': 2, 'x': 3, 'y': 4})
        self.assertEqual(s11.id, 1)
        self.assertEqual(s11.size, 2)
        self.assertEqual(s11.x, 3)
        self.assertEqual(s11.y, 4)

if __name__ == '__main__':
    unittest.main()
