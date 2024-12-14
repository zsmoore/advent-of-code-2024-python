import unittest
from solution import solve_it


class MyTestCase(unittest.TestCase):
    def test_simple(self):
        col_1 = [1, 2, 3]
        col_2 = [1, 2, 3]

        self.assertEqual(solve_it(col_1, col_2), 0)

    def test_again(self):
        col_1 = [5, 6, 7]
        col_2 = [6, 7, 8]

        self.assertEqual(solve_it(col_1, col_2), 3)

    def test_sorting(self):
        col_1 = [10, 5, 20]
        col_2 = [11, 6, 21]

        self.assertEqual(solve_it(col_1, col_2), 3)

    def test_example(self):
        col_1 = [3, 4, 2, 1, 3, 3]
        col_2 = [4, 3, 5, 3, 9 ,3]

        self.assertEqual(solve_it(col_1, col_2), 11)


if __name__ == '__main__':
    unittest.main()
