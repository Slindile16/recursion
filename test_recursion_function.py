import unittest
from recursion_function import (
    factorial, fibonacci, sum_digits, reverse_list,
    count_vowels, is_palindrome, string_repeat,
    format_nested_numbers, sum_ascii, nested_factorial_sum
)

class TestRecursionFunctions(unittest.TestCase):

    # ----------------------------
    # Factorial tests
    # ----------------------------
    def test_factorial_basic(self):
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(5), 120)
    def test_factorial_negative(self):
        with self.assertRaises(ValueError):
            factorial(-1)

    # ----------------------------
    # Fibonacci tests
    # ----------------------------
    def test_fibonacci_basic(self):
        self.assertEqual(fibonacci(6), 8)
    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-2)

    # ----------------------------
    # Sum digits
    # ----------------------------
    def test_sum_digits_basic(self):
        self.assertEqual(sum_digits(123), 6)
    def test_sum_digits_negative(self):
        with self.assertRaises(ValueError):
            sum_digits(-5)

    # ----------------------------
    # Reverse list
    # ----------------------------
    def test_reverse_list_basic(self):
        self.assertEqual(reverse_list([1, 2, 3]), [3, 2, 1])

    # ----------------------------
    # Count vowels
    # ----------------------------
    def test_count_vowels_basic(self):
        self.assertEqual(count_vowels("hello world"), 3)
        self.assertEqual(count_vowels(""), 0)

    # ----------------------------
    # Palindrome
    # ----------------------------
    def test_is_palindrome_basic(self):
        self.assertTrue(is_palindrome("Racecar"))
        self.assertFalse(is_palindrome("hello"))

    # ----------------------------
    # String repeat
    # ----------------------------
    def test_string_repeat_basic(self):
        self.assertEqual(string_repeat("ha", 3), "hahaha")
        with self.assertRaises(ValueError):
            string_repeat("ha", -1)

    # ----------------------------
    # Format nested numbers
    # ----------------------------
    def test_format_nested_numbers_basic(self):
        self.assertEqual(format_nested_numbers([1, [2, 3], 4]), "1,2,3,4")
        self.assertEqual(format_nested_numbers([]), "")

    # ----------------------------
    # Sum ASCII
    # ----------------------------
    def test_sum_ascii_basic(self):
        self.assertEqual(sum_ascii("ABC"), 198)
        self.assertEqual(sum_ascii(""), 0)

    # ----------------------------
    # Nested factorial sum
    # ----------------------------
    def test_nested_factorial_sum_basic(self):
        self.assertEqual(nested_factorial_sum([1, [2, 3]]), 9)
        self.assertEqual(nested_factorial_sum([]), 0)

if __name__ == "__main__":
    unittest.main()