# Zero-shot Prompting

## Input
    Complete the function based on intent:

    def calculate_average ( scores ) :
        total = 0
        # TODO : Complete to return average
        pass 

## Output
Here’s the completed function to calculate the average of the values in the `scores` list:

```python
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    if len(scores) == 0:
        return 0  # Avoid division by zero
    return total / len(scores)
```

This version:
- Sums up the scores,
- Checks if the list is empty to avoid dividing by zero,
- Returns the average.

# Two-shot Prompting

## Input
    Input: 3, 10, 5, 11, 4
    Output: 6.6

    Input: 5, 12, 52, 2, 4
    Output: 15

    def calculate_average ( scores ) :
        total = 0
    
## Output
To match your example outputs, it looks like you want the function to compute the **integer average** (i.e., using integer division) in the second case, but a **floating-point average** in the first. However, based on the examples:

- For input `[3, 10, 5, 11, 4]`, the sum is 33 → 33 / 5 = 6.6 ✅  
- For input `[5, 12, 52, 2, 4]`, the sum is 75 → 75 / 5 = 15 ✅  

So both are using **standard floating-point division**. Here's a completed function that behaves accordingly:

```python
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    if len(scores) == 0:
        return 0  # or raise an exception, depending on needs
    return total / len(scores)
```

### Example usage:
```python
print(calculate_average([3, 10, 5, 11, 4]))  # Output: 6.6
print(calculate_average([5, 12, 52, 2, 4]))  # Output: 15.0
```