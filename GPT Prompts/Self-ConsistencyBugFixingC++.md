# Zero-shot Prompting

## Input
    Resolve inconsistency between function name and logic:

    // Supposed to return true if x is even
    bool isOdd (int x ) {
        return x % 2 == 0; // Logic contradicts function name
    } 

## Output
To resolve the inconsistency between the function name and its logic, you have two options:

### Option 1: Rename the function to match the logic
If the logic is correct and you're checking if `x` is **even**, rename the function:

```cpp
// Returns true if x is even
bool isEven(int x) {
    return x % 2 == 0;
}
```

### Option 2: Fix the logic to match the function name
If the function name is correct and you want to check if `x` is **odd**, fix the logic:

```cpp
// Returns true if x is odd
bool isOdd(int x) {
    return x % 2 != 0;
}
```

Choose based on what the function is actually meant to do.


# One-shot Prompting

## Input
    Bad function:
    bool isEven (int x ) {
        return x % 2 != 0; // or return x % 2 == 1;
    }
    Correct function:
    bool isOdd (int x ) {
        return x % 2 != 0; // or return x % 2 == 1;
    }

    Bad Function:
    bool isOdd (int x ) {
        return x % 2 == 0;
    }
    Correct Function:

## Output
Here's the corrected version of the **bad function**:

```cpp
// Correct Function:
bool isOdd(int x) {
    return x % 2 != 0; // or return x % 2 == 1;
}
```

And if you want a **correct isEven function** for clarity:

```cpp
// Correct Function:
bool isEven(int x) {
    return x % 2 == 0;
}
```

### Summary:

| Function Name | Correct Logic                          |
|---------------|----------------------------------------|
| `isEven(x)`   | `return x % 2 == 0;`                   |
| `isOdd(x)`    | `return x % 2 != 0;` or `x % 2 == 1;`  |

This ensures both names and logic are aligned.