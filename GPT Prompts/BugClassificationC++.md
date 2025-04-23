# Zero-shot Prompting

## Input  
    Classify the type of bug in the following C++ function:
        int * getArray (int size ) {
            int arr [ size ]; // Warning : local array
            return arr ; // Bug: returning pointer to local variable
        }

## Output
The bug in the given C++ function is a **"Dangling Pointer"** bug. Here's the analysis:

```cpp
int * getArray (int size ) {
    int arr [ size ]; // Warning: local array
    return arr ; // Bug: returning pointer to local variable
}
```

### 🔍 Bug Type: **Dangling Pointer / Use After Scope**

### 🧠 Explanation:
- `arr` is a **local variable** allocated on the **stack**.
- Once `getArray()` returns, the stack frame for this function is destroyed.
- Therefore, the pointer `arr` becomes **dangling**—it points to memory that is no longer valid.
- Any attempt to use the returned pointer leads to **undefined behavior**, such as crashes or corrupted data.

---

### ✅ Correct Approach:
If you need to return an array from a function, you should:
1. Use `new` to allocate memory dynamically:
   ```cpp
   int* getArray(int size) {
       int* arr = new int[size]; // dynamic allocation
       return arr;
   }
   ```
   (Don't forget to `delete[]` it later to avoid memory leaks.)

2. Or better, use a `std::vector<int>`:
   ```cpp
   std::vector<int> getArray(int size) {
       return std::vector<int>(size);
   }
   ```
   This avoids manual memory management and is much safer.

Would you like to go over more examples of similar bugs or best practices?


# Chain-of-Thoughts Prompting

## Input
    Classify the type of bug in the following C++ function step by step:
        int * getArray (int size ) {
            int arr [ size ]; // Warning : local array
            return arr ; // Bug: returning pointer to local variable
        }

## Output
Sure! Let's walk through the C++ function **step by step** to classify the **type of bug** it contains:

---

### 🔍 Function:
```cpp
int* getArray(int size) {
    int arr[size];      // Warning: local array
    return arr;         // Bug: returning pointer to local variable
}
```

---

### ✅ Step-by-step Classification:

#### **Step 1: Understand the Declaration**
```cpp
int arr[size];
```
- This declares a **local array** named `arr` with `size` elements.
- In C++, arrays declared this way inside functions are allocated on the **stack**.
- The lifetime of `arr` is **limited to the duration of the function call**.

➡️ **Type**: Stack allocation (automatic storage duration)

---

#### **Step 2: Analyze the Return Statement**
```cpp
return arr;
```
- Here, `arr` **decays** to a pointer to its first element (i.e., `int*`).
- However, since `arr` was a **local stack variable**, this pointer will refer to memory that **no longer exists** once the function ends.

➡️ **Type**: Returning pointer to a destroyed (out-of-scope) variable

---

#### **Step 3: Identify the Bug**
- After the function returns, `arr`’s memory is **invalid**.
- Any access to the returned pointer leads to **undefined behavior**.

➡️ **Bug Type**:  
**Dangling Pointer** – a pointer that refers to a memory location that has been deallocated.

---

#### **Step 4: Result of the Bug**
- **Undefined behavior**: reading from or writing to the returned pointer may cause:
  - Crashes
  - Memory corruption
  - Unexpected output

---

### 🏷 Final Classification:
> **Bug Type**: **Dangling Pointer**  
> **Cause**: Returning a pointer to a local stack-allocated array that goes out of scope after function return.

Would you like a fixed version or to explore tools that catch this kind of bug?