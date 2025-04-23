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
Sure! Here's a prompt that would generate that exact Python code:

**Prompt:**
> Write a Python function called `is_prime(n)` that returns `True` if `n` is a prime number and `False` otherwise. The function should check if `n` is less than or equal to 1 (not prime), and for other values, it should check divisibility from 2 up to the square root of `n`. Include a comment explaining the purpose of the function.


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
### Prompt:  
Write a Python function called `is_prime(n)` that returns `True` if the input number `n` is a prime number and `False` otherwise. Include a comment describing the function's purpose, and use an efficient method that checks divisibility only up to the square root of `n`.