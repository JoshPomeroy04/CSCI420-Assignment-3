# Zero-shot Prompting

## Input
    Identify any null dereference risk:

    public int getLength ( String s ) {
        return s . length () ; // What if s is null ?
    }

## Output
Yes, this code has a **null dereference risk**.

### Problem:
In the line:
```java
return s.length(); // What if s is null ?
```
If `s` is `null`, calling `s.length()` will throw a **`NullPointerException`** at runtime.

---

### How to Fix It:
You should check if `s` is `null` before accessing its methods. Here's one way to handle it:

#### Option 1: Return 0 for null strings
```java
public int getLength(String s) {
    if (s == null) {
        return 0;
    }
    return s.length();
}
```

#### Option 2: Throw a custom exception
```java
public int getLength(String s) {
    if (s == null) {
        throw new IllegalArgumentException("Input string must not be null");
    }
    return s.length();
}
```

Which option you choose depends on your intended behavior — whether `null` is an expected case or an error.


# Role-Playing Prompting

## Input
    You are a seasoned Java developer, identify any null dereference risk:

    public int getLength ( String s ) {
        return s . length () ; // What if s is null ?
    }  

## Output
As a seasoned Java developer, I can confirm that this method contains a **null dereference risk**.

### Code Analysis:
```java
public int getLength(String s) {
    return s.length(); // What if s is null ?
}
```

### Risk:
If the parameter `s` is `null`, the method call `s.length()` will result in a **`NullPointerException`** at runtime. This is a classic example of null dereference — attempting to access a method or field on a `null` reference.

---

### Defensive Solutions:

#### ✅ Option 1: Return a default value (e.g., 0) if `s` is null
This is suitable when a `null` string is considered equivalent to an empty string:
```java
public int getLength(String s) {
    return (s != null) ? s.length() : 0;
}
```

#### ✅ Option 2: Throw an exception with a clear message
Use this when `null` is an invalid input and you want to fail fast:
```java
public int getLength(String s) {
    if (s == null) {
        throw new IllegalArgumentException("Input string must not be null");
    }
    return s.length();
}
```

---

### Best Practice:
Always **validate inputs** early, especially in public-facing APIs, to prevent undefined behavior or hard-to-trace bugs caused by null dereferencing. Consider using **`Objects.requireNonNull(s)`** for quick checks when nulls should not be allowed:
```java
import java.util.Objects;

public int getLength(String s) {
    Objects.requireNonNull(s, "Input string must not be null");
    return s.length();
}
```