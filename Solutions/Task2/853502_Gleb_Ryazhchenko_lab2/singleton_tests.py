import unittest
from Lab2.singleton import Singleton


class TestClass(metaclass=Singleton):
    pass


class SingletonTest(unittest.TestCase):
    def setUp(self):
        self.instance_a = TestClass()
        self.instance_b = TestClass()

    def test_singleton_metaclass(self):
        self.assertTrue(self.instance_a == self.instance_b)


if __name__ == '__main__':
    unittest.main()
