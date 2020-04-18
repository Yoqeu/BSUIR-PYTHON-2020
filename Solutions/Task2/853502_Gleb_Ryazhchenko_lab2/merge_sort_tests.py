import unittest
from Lab2 import merge_sort


class MergeSortTests(unittest.TestCase):
    def test_merge_sort(self):
        arr = [2, 3, 1]
        merge_sort.merge_sort(arr)
        self.assertEqual(arr, [1, 2, 3])


if __name__ == "__main__":
    unittest.main()
