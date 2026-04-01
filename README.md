# Advanced Recursion Practice Test

## Objective
Implement 10 recursive functions in Python. **No loops allowed** — recursion is mandatory. Handle invalid input as specified.  

You will implement the functions in `recursion_functions.py` and verify correctness with `test_recursion_functions.py`.

---

## Functions to Implement

### 1. `factorial(n)`
- **Description:** Returns the factorial of a non-negative integer `n`.
- **Requirements:** Raise `ValueError` if `n < 0`.
- **Example:**
  ```python
  factorial(0) -> 1
  factorial(5) -> 120


2. fibonacci(n)
Description: Returns the n-th number in the Fibonacci sequence.

Requirements: Raise ValueError if n < 0.

Example:

fibonacci(0) -> 0
fibonacci(1) -> 1
fibonacci(6) -> 8


3. sum_digits(n)
Description: Returns the sum of all digits of a non-negative integer n.

Requirements: Raise ValueError if n < 0.

Example:

sum_digits(0) -> 0
sum_digits(123) -> 6
sum_digits(4567) -> 22


4. reverse_list(lst)
Description: Recursively reverses a list lst.

Example:

reverse_list([]) -> []
reverse_list([1, 2, 3]) -> [3, 2, 1]
reverse_list(['a','b','c']) -> ['c','b','a']


5. count_vowels(s)
Description: Counts the number of vowels (a, e, i, o, u) in string s. Case-insensitive.

Example:

count_vowels("hello") -> 2
count_vowels("HELLO") -> 2
count_vowels("xyz") -> 0


6. is_palindrome(s)
Description: Checks if a string s is a palindrome. Ignore case and non-alphabetic characters.

Example:

is_palindrome("Racecar") -> True
is_palindrome("A man, a plan, a canal, Panama") -> True
is_palindrome("hello") -> False


7. string_repeat(s, n)
Description: Returns the string s repeated n times using recursion.

Requirements: Raise ValueError if n < 0.

Example:

string_repeat("ha", 3) -> "hahaha"
string_repeat("abc", 0) -> ""


8. format_nested_numbers(lst)
Description: Flattens a nested list of integers lst and returns a comma-separated string of numbers.

Example:

format_nested_numbers([1, [2, 3], 4]) -> "1,2,3,4"
format_nested_numbers([]) -> ""
format_nested_numbers([[1],[2,[3,4]]]) -> "1,2,3,4"


9. sum_ascii(s)
Description: Returns the sum of ASCII values of all characters in string s.

Example:

sum_ascii("ABC") -> 65+66+67 = 198
sum_ascii("") -> 0
sum_ascii("hello") -> 104+101+108+108+111 = 532


10. nested_factorial_sum(lst) 
Description: Takes a list lst of integers (may contain nested lists) and returns the sum of their factorials.

Example:

nested_factorial_sum([1, [2, 3]]) -> 1! + 2! + 3! = 1 + 2 + 6 = 9
nested_factorial_sum([]) -> 0
nested_factorial_sum([[1,2],[3,4]]) -> 1!+2!+3!+4! = 1+2+6+24 = 33
Requirements

Recursion only: Do not use loops (for, while) in any function.

Error handling: Raise ValueError for invalid input (negative numbers for factorial, fibonacci, sum_digits, string_repeat).

Graceful handling: Functions should handle empty strings or empty lists correctly.

Testing: Use test_recursion_functions.py to verify correctness.

Testing

Run the unit tests to check your solutions:

python -m unittest test_recursion_functions.py

All tests must pass for full credit.