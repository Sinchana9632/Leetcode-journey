# 412. Fizz Buzz
## Difficulty: Easy

### Problem Description
Given an integer `n`, return a string array `answer` (1-indexed) where:
- `answer[i] == "FizzBuzz"` if `i` is divisible by 3 and 5.
- `answer[i] == "Fizz"` if `i` is divisible by 3.
- `answer[i] == "Buzz"` if `i` is divisible by 5.
- `answer[i] == i` (as a string) if none of the above conditions are true.

### Logic Explained
- **Day 1 Focus:** Conditional statements and the Modulo (`%`) operator.
- **Key Insight:** We must check for divisibility by **15** (both 3 and 5) first to avoid logic errors.

### Performance
- **Language:** Python 3
- **Runtime:** Faster than ~85% of submissions.