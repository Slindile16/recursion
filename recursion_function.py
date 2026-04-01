"""
recursion_function.py

Implement recursive functions as described in the README.
"""

# ----------------------------
# Existing functions
# ----------------------------
def factorial(n):
    """Return factorial of n using recursion. Raise ValueError if n < 0"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    """Return the n-th Fibonacci number using recursion. Raise ValueError if n < 0"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_digits(n):
    """Return the sum of digits of a non-negative integer n using recursion. Raise ValueError if n < 0"""
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    return n % 10 + sum_digits(n // 10)


def reverse_list(lst):
    """Recursively reverse a list"""
    if lst == []:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])

# ----------------------------
# New functions
# ----------------------------
def count_vowels(s):
    """
    Recursively count the number of vowels in a string s.
    Example: count_vowels("hello") -> 2
    """
    if s == "":
        return 0
    first = s[0].lower()
    if first in "aeiou":
        return 1 + count_vowels(s[1:])
    return count_vowels(s[1:])

def is_palindrome(s):
    """
    Recursively check if a string s is a palindrome.
    Ignore case and non-alphabetic characters.
    Example: is_palindrome("Racecar") -> True
    """
    # Use two-pointer recursion skipping non-alphabetic characters
    def helper(l, r):
        if l >= r:
            return True
        if not s[l].isalpha():
            return helper(l + 1, r)
        if not s[r].isalpha():
            return helper(l, r - 1)
        if s[l].lower() != s[r].lower():
            return False
        return helper(l + 1, r - 1)

    return helper(0, len(s) - 1)


def string_repeat(s, n):
    """
    Recursively repeat a string s, n times.
    Example: string_repeat("ha", 3) -> "hahaha"
    Raise ValueError if n < 0
    """
    if n < 0:
        raise ValueError("n must be non-negative")  # error check
    if n == 0:  
          return ""# base case: repeating 0 times returns empty string
    return s + string_repeat(s, n - 1)  # recursive step: add s one time, then repeat n-1
# print(string_repeat("ha", 6))

def format_nested_numbers(lst):
    """
    Recursively take a nested list of integers and return a string of all numbers
    joined by commas. 
    Example: format_nested_numbers([1, [2, 3], 4]) -> "1,2,3,4"
    """
    def helper(arr):
        if arr == []:
            return []
        head = arr[0]
        tail = arr[1:]
        if isinstance(head, list):
            return helper(head) + helper(tail)
        else:
            return [str(head)] + helper(tail)

    flattened = helper(lst)
    return ",".join(flattened) if flattened else ""

def sum_ascii(s):
    """
    Recursively return the sum of ASCII values of all characters in a string s.
    Example: sum_ascii("ABC") -> 65+66+67=198
    """
    if s == "":
        return 0
    return ord(s[0]) + sum_ascii(s[1:])

def nested_factorial_sum(lst):
    """
    Recursively take a list of integers (may contain nested lists) and return
    the sum of their factorials.
    Example: nested_factorial_sum([1, [2, 3]]) -> 1! + 2! + 3! = 1 + 2 + 6 = 9
    """
    if lst == []:
        return 0
    head = lst[0]
    tail = lst[1:]
    if isinstance(head, list):
        return nested_factorial_sum(head) + nested_factorial_sum(tail)
    else:
        return factorial(head) + nested_factorial_sum(tail)