# Zero-shot Prompting

## Input
    Identify and fix the bug:

    function isEven ( n ) {
        return n % 2; // Returns 1 or 0 , not true / false
    } 

## Output
You're spot on! The bug in the `isEven` function is that the modulo operator (`%`) returns the remainder of the division. For an even number, the remainder when divided by 2 is 0, and for an odd number, it's 1. In JavaScript, 0 is considered "falsy" and 1 is considered "truthy," but they are not the boolean values `true` and `false`.

Here's the corrected version of the function:

```javascript
function isEven(n) {
  return n % 2 === 0; // Returns true if the remainder is 0, false otherwise
}
```

**Explanation of the fix:**

By comparing the result of `n % 2` to 0 using the strict equality operator (`===`), the function now explicitly returns a boolean value:

* If `n` is even, `n % 2` will be 0, and `0 === 0` evaluates to `true`.
* If `n` is odd, `n % 2` will be 1, and `1 === 0` evaluates to `false`.

This ensures the function correctly identifies whether a number is even or not by returning a proper boolean value.


# Prompt Chaining

## Input 1
    Only identify the bug:

    function isEven ( n ) {
        return n % 2; // Returns 1 or 0 , not true / false
    } 

## Output 1
The bug is that the function returns the remainder of the division by 2 (which will be `0` or `1`), instead of a boolean value (`true` or `false`).

## Input 2
    Now fix the bug

## Output 2
```javascript
function isEven ( n ) {
  return n % 2 === 0; // Returns true if the remainder is 0, false otherwise
}
```

The bug is fixed by explicitly comparing the result of the modulo operation (`n % 2`) to `0` using the strict equality operator (`===`). This ensures the function returns a boolean value (`true` for even numbers, `false` for odd numbers).