# Zero-shot Prompting

## Input
    Complete the recursive function for Fibonacci:

    def fibonacci ( n ) :
        # TODO : Base cases and recursive call
        pass 

## Output
```python
def fibonacci(n):
    """
    Calculates the nth Fibonacci number recursively.

    Args:
        n: The index of the desired Fibonacci number (non-negative integer).

    Returns:
        The nth Fibonacci number.
    """
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive call
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example Usage:
print(f"fibonacci(0) = {fibonacci(0)}")
print(f"fibonacci(1) = {fibonacci(1)}")
print(f"fibonacci(2) = {fibonacci(2)}")
print(f"fibonacci(3) = {fibonacci(3)}")
print(f"fibonacci(4) = {fibonacci(4)}")
print(f"fibonacci(5) = {fibonacci(5)}")
print(f"fibonacci(10) = {fibonacci(10)}")
```

**Explanation:**

1.  **Base Cases:**
    * `if n == 0:`: The 0th Fibonacci number is defined as 0. This is our first base case, which stops the recursion for the smallest input.
    * `elif n == 1:`: The 1st Fibonacci number is defined as 1. This is our second base case.

2.  **Recursive Call:**
    * `else:`: For any `n` greater than 1, the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers. This is the core of the recursive definition.
    * `return fibonacci(n - 1) + fibonacci(n - 2)`: The function calls itself twice with smaller inputs (`n - 1` and `n - 2`) and returns the sum of the results. This process continues until it reaches the base cases (n=0 or n=1), at which point the recursion unwinds, and the final result is calculated.

**How it Works (Example for `fibonacci(4)`):**

1.  `fibonacci(4)` calls `fibonacci(3)` and `fibonacci(2)`
2.  `fibonacci(3)` calls `fibonacci(2)` and `fibonacci(1)`
3.  `fibonacci(2)` calls `fibonacci(1)` and `fibonacci(0)`
4.  `fibonacci(1)` returns `1` (base case)
5.  `fibonacci(0)` returns `0` (base case)
6.  `fibonacci(2)` returns `1 + 0 = 1`
7.  `fibonacci(1)` returns `1` (base case)
8.  `fibonacci(3)` returns `1 + 1 = 2`
9.  `fibonacci(2)` calls `fibonacci(1)` and `fibonacci(0)` (again)
10. `fibonacci(1)` returns `1`
11. `fibonacci(0)` returns `0`
12. `fibonacci(2)` returns `1 + 0 = 1`
13. `fibonacci(4)` returns `2 + 1 = 3`

**Note on Efficiency:**

While this recursive solution is clear and directly reflects the mathematical definition of the Fibonacci sequence, it is not the most efficient way to calculate Fibonacci numbers, especially for larger values of `n`. This is because it involves redundant calculations. For example, `fibonacci(2)` is calculated multiple times in the example above. For better performance with larger inputs, iterative approaches (using loops) or memoization (caching results of subproblems) are generally preferred.


# Chain-of-Thoughts Prompting

## Input 
    Step by step complete the recursive function for Fibonacci:

    def fibonacci ( n ) :
        # TODO : Base cases and recursive call
        pass 

## Output
Okay, let's complete the recursive `fibonacci` function step by step:

**Step 1: Define the function signature (already provided)**

```python
def fibonacci(n):
    # TODO : Base cases and recursive call
    pass
```

This line defines a function named `fibonacci` that takes one argument, `n`, which represents the index of the Fibonacci number we want to calculate.

**Step 2: Implement the first base case (n = 0)**

The 0th Fibonacci number is defined as 0. We need to add a conditional statement to handle this:

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    # TODO : Second base case and recursive call
    pass
```

If the input `n` is 0, the function immediately returns 0, stopping the recursion for this specific input.

**Step 3: Implement the second base case (n = 1)**

The 1st Fibonacci number is defined as 1. We need to add another conditional statement to handle this:

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # TODO : Recursive call
    pass
```

If the input `n` is 1, the function immediately returns 1, stopping the recursion for this specific input as well.

**Step 4: Implement the recursive call (n > 1)**

For any value of `n` greater than 1, the nth Fibonacci number is the sum of the (n-1)th and (n-2)th Fibonacci numbers. This is where the recursion happens:

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive call
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

If `n` is greater than 1, the function calls itself twice: once with `n - 1` and once with `n - 2`. The results of these two recursive calls are then added together and returned as the nth Fibonacci number.

**Complete Function:**

Putting it all together, the completed recursive `fibonacci` function is:

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive call
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
```

This function will now correctly calculate the nth Fibonacci number using recursion. Remember that for larger values of `n`, this recursive approach can be inefficient due to repeated calculations.