import unittest

from Lab2.vector import Vector


class TestVectorMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(Vector.__add__(Vector((1, 2, 3)), Vector((1, 2, 3))), Vector((2, 4, 6)))

    def test_mul(self):
        self.assertEqual(Vector.__mul__(Vector((1, -7, 5)), Vector((1, 3, 3))), -5)

    def test_scalar_mul(self):
        self.assertEqual(Vector.__mul__(Vector((1, 2, 3)), 2), Vector((2, 4, 6)))

    def test_sub(self):
        self.assertEqual(Vector.__sub__(Vector((2, 3, 4)), Vector((1, 2, 3))), Vector((1, 1, 1)))

    def test_equal(self):
        self.assertEqual(Vector.__eq__(Vector((1, 2, 3)), Vector((1, 2, 3))), True)

    def test_len(self):
        self.assertEqual(Vector.__len__(Vector((1, 2, 3))), 3)

    def test_string_reformat(self):
        self.assertEqual(Vector.__repr__(Vector((1, 2, 3))), 'Vector((1, 2, 3))')


if __name__ == '__main__':
    unittest.main()
