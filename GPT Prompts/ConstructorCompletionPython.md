# Zero-shot Prompting

## Input
    Complete the class constructor:

    class Person :
        def __init__ ( self ) :
            # TODO : Add name , age , and optional email
            pass

## Output
Here’s a completed version of the `Person` class constructor, adding `name`, `age`, and an optional `email` parameter with a default value of `None`:

```python
class Person:
    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email
```

### Example usage:
```python
p1 = Person("Alice", 30)
p2 = Person("Bob", 25, "bob@example.com")
```

Let me know if you want validation or default values added!


# Chain-of-Thoughts Prompting

## Input 
    Step by step complete the class constructor:

    class Person :
        def __init__ ( self ) :
            # TODO : Add name , age , and optional email
            pass

## Output
Sure! Let's complete the constructor **step by step**, adding `name`, `age`, and an optional `email` parameter.

---

### ✅ Step 1: Add parameters to the constructor
We need the constructor to accept three parameters: `name`, `age`, and `email`. The `email` should be optional.

```python
def __init__(self, name, age, email=None):
```

---

### ✅ Step 2: Assign the parameters to instance variables  
We’ll store the values inside the object using `self`.

```python
self.name = name
self.age = age
self.email = email
```

---

### ✅ Step 3: Put it all together inside the class

```python
class Person:
    def __init__(self, name, age, email=None):
        self.name = name
        self.age = age
        self.email = email
```

---

### ✅ Example usage:

```python
p1 = Person("Alice", 30)
p2 = Person("Bob", 25, "bob@example.com")

print(p1.name, p1.age, p1.email)  # Alice 30 None
print(p2.name, p2.age, p2.email)  # Bob 25 bob@example.com
```

Let me know if you want to add input validation or default values!