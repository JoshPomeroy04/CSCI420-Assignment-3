# Zero-shot Prompting

## Input  
    Complete the Python function using regex to validate basic email addresses:
            def is_valid_email ( email ):
                # TODO : Complete using regex
                pass

## Output: 
Here's a complete version of the `is_valid_email` function using regular expressions to validate **basic email addresses**:

```python
import re

def is_valid_email(email):
    # Basic regex for email validation
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(pattern, email) is not None
```

### Explanation:
- `^` and `$` – anchor the regex to start and end of the string.
- `[a-zA-Z0-9_.+-]+` – local part before the `@`, allowing letters, digits, underscore, dot, plus, and hyphen.
- `@` – the literal `@` symbol.
- `[a-zA-Z0-9-]+` – domain name (e.g., `gmail`).
- `\.` – literal dot before the TLD.
- `[a-zA-Z0-9-.]+` – TLD (e.g., `com`, `co.uk`).

Let me know if you want to make it stricter (e.g., disallow consecutive dots or require at least 2-letter TLDs).


# Chain-of-Thoughts Prompting

## Input 
    Complete the Python function step by step, using regex to validate basic email addresses:
        def is_valid_email ( email ):
            # TODO : Complete using regex
            pass
    
## Output
Sure! Let’s complete the `is_valid_email` function **step by step** using regex to validate basic email addresses:

---

### ✅ **Step 1: Import the `re` module**
We need the `re` module to use regular expressions in Python.

```python
import re
```

---

### ✅ **Step 2: Define the function**
This is already given, but let’s confirm the structure:

```python
def is_valid_email(email):
    # TODO: Complete using regex
    pass
```

---

### ✅ **Step 3: Write a regex pattern for a basic email**
A **basic** email has:
- A local part (letters, digits, underscores, dots, hyphens)
- An `@` symbol
- A domain (letters, digits, hyphens)
- A `.` and a top-level domain (like `.com`, `.org`)

So our pattern will be:

```python
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
```

---

### ✅ **Step 4: Use `re.match()` to test the pattern**
This will check if the email matches from the start (`^`) to the end (`$`).

```python
match = re.match(pattern, email)
```

---

### ✅ **Step 5: Return True if it matches, False otherwise**

```python
return match is not None
```

---

### ✅ **Final Function**

```python
import re

def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    match = re.match(pattern, email)
    return match is not None
```

Let me know if you want to add stricter checks (like no double dots, or requiring the TLD to be at least 2 characters).