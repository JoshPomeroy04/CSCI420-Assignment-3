# Zero-shot Prompting

## Input
    Write a prompt that could generate the following Python code:

    # This function checks if a number is prime
    def is_prime ( n ) :
        if n <= 1:
            return False
        for i in range (2 , int( n **0.5) +1) :
            if n % i == 0:
                return False
        return True

## Output
Here are a few prompt options that could generate the Python code you provided, varying slightly in their phrasing:

**Option 1 (Direct and Functional):**

> Write a Python function called `is_prime` that takes an integer `n` as input and returns `True` if `n` is a prime number and `False` otherwise. The function should include a check for numbers less than or equal to 1 and optimize the primality test by only checking divisibility up to the square root of `n`.

**Option 2 (Slightly More Descriptive):**

> Create a Python function that determines if a given integer is a prime number. The function should be named `is_prime` and accept a single integer argument. Ensure the function handles the base case where the number is less than or equal to 1. For efficiency, the divisibility check should only iterate up to the integer part of the square root of the input number.

**Option 3 (Focusing on the Logic):**

> Generate Python code for a function `is_prime(n)` that implements the standard primality test. This function should first handle the case of `n` being less than or equal to 1. Then, it should iterate through potential divisors from 2 up to the square root of `n`. If any of these divisors evenly divide `n`, the function should return `False`. Otherwise, if the loop completes without finding a divisor, the function should return `True`.

**Option 4 (Concise):**

> Write a Python function `is_prime(n)` that efficiently checks if an integer `n` is prime.

All of these prompts aim to guide the language model towards generating the specific Python code you provided by highlighting the key aspects of the function: its name, input, output, the base case for non-prime numbers, and the optimization using the square root.


# One-shot Prompting

## Input
    ### Code:
    def is_even(n):
        return n % 2 == 0
    ### Prompt:
    Write a Python function to check if a number is even

    ### Code:
    # This function checks if a number is prime
    def is_prime ( n ) :
        if n <= 1:
            return False
    for i in range (2 , int( n **0.5) +1) :
        if n % i == 0:
            return False
    return True 
    ### Prompt:

## Output
Write a Python function to check if a number is prime, including handling edge cases and optimizing for efficiency.