import unittest
from Lab2 import json_tests, merge_sort_tests, singleton_tests, vector_tests, decorator_tests


def main():
    suite_sort = unittest.TestLoader().loadTestsFromModule(merge_sort_tests)
    suite_json = unittest.TestLoader().loadTestsFromModule(json_tests)
    suite_vector = unittest.TestLoader().loadTestsFromModule(vector_tests)
    suite_singleton = unittest.TestLoader().loadTestsFromModule(singleton_tests)
    suite_decorator = unittest.TestLoader().loadTestsFromModule(decorator_tests)
    all_tests = unittest.TestSuite([suite_json, suite_sort, suite_vector,
                                    suite_singleton, suite_decorator])
    unittest.TextTestRunner(verbosity=2).run(all_tests)
    pass
