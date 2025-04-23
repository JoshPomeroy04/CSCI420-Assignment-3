# Zero-shot Prompting

## Input 
    Improve the parser to support quoted fields: 

    def parse_csv_line ( line ) :
        return line . split (’,’) # Incomplete : doesn ’t handle quoted fields

## Output
To correctly handle quoted fields in a CSV line—where commas inside quotes shouldn't split the field—you need to account for these cases during parsing. Here's an improved version of the `parse_csv_line` function:

```python
import csv
from io import StringIO

def parse_csv_line(line):
    # Use Python's built-in csv module for proper handling
    reader = csv.reader(StringIO(line), skipinitialspace=True)
    return next(reader)
```

### Example usage:
```python
line = 'John, "Smith, Jr.", 30, "New York, NY"'
print(parse_csv_line(line))
```

### Output:
```
['John', 'Smith, Jr.', '30', 'New York, NY']
```

### Why this works:
- The `csv` module properly handles:
  - Quoted fields
  - Escaped quotes within fields
  - Whitespace after delimiters (when `skipinitialspace=True` is used)

Let me know if you need a version without using the `csv` module!


# Chain-of-Thoughts Prompting

## Input 
    Step by step, improve the parser to support quoted fields: 

    def parse_csv_line ( line ) :
        return line . split (’,’) # Incomplete : doesn ’t handle quoted fields

## Output
Sure! Let's improve the `parse_csv_line` function step by step **without using the `csv` module**, so we can see exactly how quoted fields are handled manually.

---

### **Step 1: Start with a basic loop instead of `split(',')`**

We’ll build the fields manually by iterating over each character and tracking when we’re inside quotes.

```python
def parse_csv_line(line):
    fields = []
    field = ''
    in_quotes = False

    for char in line:
        if char == '"':
            in_quotes = not in_quotes  # Toggle quote state
        elif char == ',' and not in_quotes:
            fields.append(field)
            field = ''
        else:
            field += char

    fields.append(field)  # Add the last field
    return fields
```

---

### **Step 2: Handle escaped quotes (e.g., `""` inside quoted field)**

We’ll need to look ahead when we see a quote to detect if it’s a double quote escape (`""`), which should be treated as a literal quote.

```python
def parse_csv_line(line):
    fields = []
    field = ''
    in_quotes = False
    i = 0

    while i < len(line):
        char = line[i]
        if char == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                field += '"'  # Add escaped quote
                i += 1        # Skip next quote
            else:
                in_quotes = not in_quotes  # Toggle quoted state
        elif char == ',' and not in_quotes:
            fields.append(field)
            field = ''
        else:
            field += char
        i += 1

    fields.append(field)
    return fields
```

---

### **Step 3: Strip optional surrounding whitespace and quotes**

Some CSV formats want to strip quotes or leading/trailing spaces from unquoted fields.

```python
def parse_csv_line(line):
    fields = []
    field = ''
    in_quotes = False
    i = 0

    while i < len(line):
        char = line[i]
        if char == '"':
            if in_quotes and i + 1 < len(line) and line[i + 1] == '"':
                field += '"'  # Add escaped quote
                i += 1
            else:
                in_quotes = not in_quotes
        elif char == ',' and not in_quotes:
            fields.append(field)
            field = ''
        else:
            field += char
        i += 1

    fields.append(field)

    # Optional cleanup: strip outer quotes and surrounding spaces
    def clean(f):
        f = f.strip()
        if f.startswith('"') and f.endswith('"'):
            f = f[1:-1].replace('""', '"')
        return f

    return [clean(f) for f in fields]
```

---

### ✅ Example:

```python
parse_csv_line('John,"Smith, Jr.",30,"New York, NY","He said ""Hello"""')
```

**Output:**

```python
['John', 'Smith, Jr.', '30', 'New York, NY', 'He said "Hello"']
```

Let me know if you'd like this converted into a class, support for different delimiters, or multiline parsing!