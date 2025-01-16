#!/usr/bin/python3
import sys

# Function Description:
# The `factorial` function calculates the factorial of a given non-negative integer `n` using recursion.
# The factorial of a number is the product of all positive integers less than or equal to that number.
# For example, factorial(4) = 4 * 3 * 2 * 1 = 24.
# Factorial of 0 is defined as 1 (base case).

# Parameters:
# n (int): A non-negative integer for which the factorial needs to be calculated.
#          The function will recursively call itself with decreasing values of `n` until `n` reaches 0.

# Returns:
# int: The factorial of the input number `n`. If `n == 0`, it returns 1.
# If `n > 0`, it returns `n * factorial(n-1)`.

def factorial(n):
    if n == 0:  # Base case: factorial(0) = 1
        return 1
    else:
        return n * factorial(n-1)  # Recursive case: n * factorial of (n-1)

# Get the input number from command-line arguments and calculate its factorial
f = factorial(int(sys.argv[1]))  # Convert input to integer and call factorial function

# Print the calculated factorial
print(f)
