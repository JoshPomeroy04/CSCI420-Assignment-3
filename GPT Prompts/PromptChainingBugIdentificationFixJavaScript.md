# Zero-shot Prompting

## Input
    Identify and fix the bug:

    function isEven ( n ) {
        return n % 2; // Returns 1 or 0 , not true / false
    } 

## Output
The bug here is that `n % 2` returns `0` for even numbers and `1` for odd numbers, but the function is expected to return a **Boolean** (`true` for even, `false` for odd), not an integer.

### ✅ Fixed version:
```javascript
function isEven(n) {
    return n % 2 === 0;
}
```

### 🔍 Explanation:
- `n % 2 === 0` evaluates to `true` if `n` is even, and `false` otherwise — exactly what the function name `isEven` implies.


# Prompt Chaining

## Input 1
    Only identify the bug:

    function isEven ( n ) {
        return n % 2; // Returns 1 or 0 , not true / false
    } 

## Output 1
The bug is that the function returns `1` or `0` instead of `true` or `false`.

## Input 2
    Now fix the bug

## Output 2
```javascript
function isEven(n) {
    return n % 2 === 0;
}
```