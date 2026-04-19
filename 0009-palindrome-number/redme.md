# 9. Palindrome Number
## Difficulty: Easy

### Problem Description
Given an integer `x`, return `true` if `x` is a palindrome, and `false` otherwise.
An integer is a palindrome when it reads the same forward and backward.

### Logic Explained
- **Day 2 Focus:** Digit manipulation without converting the integer to a string.
- **The "Peeling" Method:**
  1. Used `x % 10` to extract the last digit.
  2. Used `reversed_value * 10 + digit` to build the number backward.
  3. Used `x // 10` to remove the last digit.
- **Constraints:** Handled negative numbers immediately as they cannot be palindromes.

### Performance
- **Language:** Python 3
- **Runtime:** 10 ms
- **Memory:** 12.4 MB