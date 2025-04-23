# Zero-shot Prompting

## Input
    Complete the recursive function for Fibonacci:

    def fibonacci ( n ) :
        # TODO : Base cases and recursive call
        pass 

## Output
Sure! Here's a complete recursive implementation of the Fibonacci function:

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive call
    return fibonacci(n - 1) + fibonacci(n - 2)
```

This function returns the nth Fibonacci number using a simple recursive approach. Let me know if you want a more efficient version using memoization or iteration!

# Chain-of-Thoughts Prompting

## Input 
    Step by step complete the recursive function for Fibonacci:

    def fibonacci ( n ) :
        # TODO : Base cases and recursive call
        pass 

## Output
Let's complete the `fibonacci(n)` function step by step:

---

### 🔹 Step 1: Understand the Fibonacci Sequence  
The Fibonacci sequence is defined as:
- **fibonacci(0) = 0**
- **fibonacci(1) = 1**
- For **n ≥ 2**:  
  **fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)**

---

### 🔹 Step 2: Define the base cases  
These are the conditions that stop the recursion:

```python
if n == 0:
    return 0
elif n == 1:
    return 1
```

---

### 🔹 Step 3: Add the recursive case  
If `n` is greater than 1, we return the sum of the two previous Fibonacci numbers:

```python
return fibonacci(n - 1) + fibonacci(n - 2)
```

---

### 🔹 Step 4: Full function

Now putting it all together:

```python
def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case
    return fibonacci(n - 1) + fibonacci(n - 2)
```

Let me know if you'd like to make it faster using memoization or iteration!