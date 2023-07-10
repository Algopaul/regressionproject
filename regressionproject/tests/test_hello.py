import unittest
from parameterized import parameterized
from regressionproject import base


class TestHello(unittest.TestCase):
    def test_is_string(self):
        s = base.hello()
        self.assertTrue(isinstance(s, str))
        pass


class TestAddTwo(unittest.TestCase):
    @parameterized.expand(
        [
            ("integer_test", 3, 5),
            ("float_test", 1.5, 3.5),
            ("negative number", -1.6, 0.4),
        ]
    )
    def test_add_two(self, name, x, expected_result):
        result = base.addTwo(x)
        self.assertAlmostEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()
