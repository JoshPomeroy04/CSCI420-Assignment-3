# Zero-shot Prompting

## Input
    Complete the function based on intent:

    def calculate_average ( scores ) :
        total = 0
        # TODO : Complete to return average
        pass 

## Output
```python
def calculate_average ( scores ) :
  total = 0
  if not scores:
    return 0
  for score in scores:
    total += score
  average = total / len(scores)
  return average
```

# Two-shot Prompting

## Input
    Input: 3, 10, 5, 11, 4
    Output: 6.6

    Input: 5, 12, 52, 2, 4
    Output: 15

    def calculate_average ( scores ) :
        total = 0
    
## Output
```python
def calculate_average ( scores ) :
  total = 0
  if not scores:
    return 0
  for score in scores:
    total += score
  average = total / len(scores)
  return average
```