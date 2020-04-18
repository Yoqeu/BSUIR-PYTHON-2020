import unittest
import decorator
import inspect


class DecoratorTests(unittest.TestCase):
    def test_logarifm(self):
        self.assertEqual(decorator.logarifm(4), 2)

    def test_decorator(self):
        self.assertEqual(inspect.isfunction(decorator.decorator(decorator.logarifm)), True)


if __name__ == "__main__":
    unittest.main()