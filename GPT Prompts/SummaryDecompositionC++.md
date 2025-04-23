# Zero-shot Prompting

## Input
    Decompose the high-level comment/summary into logical steps:

    // Function that validates an input , calculates square , and returns result
    int process (int x ) {
    if ( x < 0) return -1;
        return x * x ;
    }

## Output
Sure! Here's the decomposition of the high-level comment into logical steps:

1. **Validate the input**:  
   Check if the input `x` is less than 0. If so, return -1 to indicate invalid input.

2. **Calculate the square**:  
   If the input is valid, compute the square of `x` (i.e., `x * x`).

3. **Return the result**:  
   Return the squared value as the final result.

Each step maps directly to a clear line or logic in the function.


# Chain-of-Thoughts Prompting

## Input 
    Step by step, decompose the high-level comment/summary into logical steps:

    // Function that validates an input , calculates square , and returns result
    int process (int x ) {
    if ( x < 0) return -1;
        return x * x ;
    }

## Output
Step by step, let's decompose the high-level comment into logical steps that match the function behavior:

---

### High-Level Summary:
**"Function that validates an input, calculates square, and returns result"**

---

### Step-by-Step Decomposition:

1. **Input Validation**  
   - Check if the input `x` is a negative number (`x < 0`).
   - If the input is invalid (i.e., negative), return `-1` to indicate an error or special condition.

2. **Calculation**  
   - If the input passes validation (i.e., it is non-negative), compute the square of `x` using `x * x`.

3. **Return the Result**  
   - Return the squared value as the final result of the function.

---

Each step in this decomposition directly corresponds to a line or concept in the actual code implementation.