# Zero-shot Prompting

## Input  
    Complete the Python function using regex to validate basic email addresses:
            def is_valid_email ( email ):
                # TODO : Complete using regex
                pass

## Output: 
```python
import re

def is_valid_email(email):
    """
    Validates basic email addresses using regex.

    Args:
        email: The email address string to validate.

    Returns:
        True if the email address matches the basic pattern, False otherwise.
    """
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return bool(re.fullmatch(pattern, email))
```

This function employs the `re` module in Python to perform regular expression matching. The regex pattern `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$` is designed to check for the following basic email structure:

* `^[a-zA-Z0-9._%+-]+`: Matches one or more alphanumeric characters, periods, underscores, percentage signs, plus signs, or hyphens at the beginning of the string (local part of the email).
* `@`: Matches the "@" symbol, which separates the local part from the domain.
* `[a-zA-Z0-9.-]+`: Matches one or more alphanumeric characters, periods, or hyphens (domain name).
* `\.`: Matches a literal dot ".".
* `[a-zA-Z]{2,}$`: Matches two or more alphabetic characters at the end of the string (top-level domain).

The `re.fullmatch()` function attempts to match the entire input string against the pattern. It returns a match object if the entire string conforms to the pattern, and `None` otherwise. The `bool()` function then converts this result to a boolean value: `True` if there's a match (valid email), and `False` if there's no match (invalid email).

Keep in mind that this regex provides a basic level of email validation. More sophisticated email validation often involves checking for the existence of the domain, handling internationalized domain names, and adhering to more rigorous RFC specifications.


# Chain-of-Thoughts Prompting

## Input 
    Complete the Python function step by step, using regex to validate basic email addresses:
        def is_valid_email ( email ):
            # TODO : Complete using regex
            pass
    
## Output
```python
import re

def is_valid_email(email):
    """
    Validates basic email addresses using regex, step by step.

    Args:
        email: The email address string to validate.

    Returns:
        True if the email address matches the basic pattern, False otherwise.
    """
    # Step 1: Define the regular expression pattern for a basic email address.
    # This pattern checks for:
    # - One or more alphanumeric characters, periods, underscores, percentage signs, plus signs, or hyphens
    #   at the beginning (local part).
    # - Followed by an "@" symbol.
    # - Followed by one or more alphanumeric characters, periods, or hyphens (domain name).
    # - Followed by a literal dot ".".
    # - Followed by two or more alphabetic characters at the end (top-level domain).
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Step 2: Use the 're.fullmatch()' function to attempt to match the entire
    # email string against the defined pattern.
    # 're.fullmatch()' returns a match object if the entire string matches the pattern,
    # and None otherwise.
    match = re.fullmatch(pattern, email)

    # Step 3: Check if a match object was returned.
    # If 'match' is not None, it means the entire email string conforms to the pattern.
    if match:
        return True
    else:
        return False

# Example usage:
print(is_valid_email("test@example.com"))
print(is_valid_email("user.name@subdomain.example.co.uk"))
print(is_valid_email("invalid-email"))
print(is_valid_email("another@invalid"))
print(is_valid_email("@missinglocal.com"))
print(is_valid_email("local.missingat"))
```

In this step-by-step breakdown:

1.  **Import `re`:** We start by importing the `re` module, which provides regular expression operations.
2.  **Define the Regex Pattern:** We create the regular expression pattern as a raw string (`r"..."`). The pattern is designed to capture the fundamental structure of an email address.
3.  **Use `re.fullmatch()`:** The `re.fullmatch()` function is crucial here. It attempts to match the *entire* input `email` string against the `pattern`. If the whole string matches, it returns a match object; otherwise, it returns `None`.
4.  **Check for a Match:** We then check if the `match` object is not `None`. If it's not `None`, it signifies that the email address fully conforms to our defined pattern, and we return `True`.
5.  **Return `False` if No Match:** If `re.fullmatch()` returns `None`, it means the email address does not match the pattern, and we return `False`.

The example usage at the end demonstrates how to use the `is_valid_email` function with various email address strings.