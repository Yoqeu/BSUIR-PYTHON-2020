import unittest
import json

from Lab2 import from_json
from Lab2.to_json import from_string
from Lab2.from_json import to_string


class TestJsonMethods(unittest.TestCase):
    def test_empty_object_from(self):
        self.assertEqual(from_string('{}'), {})

    def test_basic_object_from(self):
        self.assertEqual(from_string('{"foo":"bar"}'), {"foo": "bar"})

    def test_basic_number_from(self):
        self.assertEqual(from_string('{"foo":1}'), {"foo": 1})

    def test_basic_whitespace_from(self):
        self.assertEqual(from_string('{ "foo" : [1, 2, "three"] }'), {"foo": [1, 2, "three"]})

    def test_basic_object_to(self):
        self.assertEqual(to_string({"foo": "bar"}), '{"foo": "bar"}')

    def test_basic_number_to(self):
        self.assertEqual(to_string({"foo": 1}), '{"foo": 1}')

    def test_basic_whitespace_to(self):
        self.assertEqual(to_string({"foo": [1, 2, "three"]}), '{"foo": [1, 2, "three"]}')


if __name__ == '__main__':
    unittest.main()
