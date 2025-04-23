# Zero-shot Prompting

## Input
    Complete the binary search implementation:

    public int binarySearch ( int [] arr , int target ) {
        int left = 0 , right = arr . length - 1;
        while ( left <= right ) {
            int mid = ( left + right ) / 2;
            // TODO : Compare and adjust bounds
        }
        return -1;
    } 

## Output
Here is the completed implementation of the binary search algorithm:

```java
public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = (left + right) / 2;

        if (arr[mid] == target) {
            return mid; // Target found
        } else if (arr[mid] < target) {
            left = mid + 1; // Search right half
        } else {
            right = mid - 1; // Search left half
        }
    }
    return -1; // Target not found
}
```

### Explanation:
- **mid = (left + right) / 2**: finds the middle index.
- **arr[mid] == target**: match found.
- **arr[mid] < target**: discard left half, move `left` up.
- **arr[mid] > target**: discard right half, move `right` down.
- Returns `-1` if the target is not found in the array.

# Chain-of-Thoughts Prompting

## Input
    Step by step complete the binary search implementation:

    public int binarySearch ( int [] arr , int target ) {
        int left = 0 , right = arr . length - 1;
        while ( left <= right ) {
            int mid = ( left + right ) / 2;
            // TODO : Compare and adjust bounds
        }
        return -1;
    } 

## Output
Sure! Let's walk through the process step by step and complete your binary search implementation:

---

### 🧠 Step 1: Find the middle index

This part is already done:
```java
int mid = (left + right) / 2;
```
This calculates the index of the middle element between `left` and `right`.

---

### 🧠 Step 2: Check if the middle element is the target

Add this condition after calculating `mid`:
```java
if (arr[mid] == target) {
    return mid;
}
```
If the value at `mid` is equal to the `target`, we found it! Return the index.

---

### 🧠 Step 3: Decide which half to search next

If the middle value is **less than** the target, the target must be in the **right half**:
```java
else if (arr[mid] < target) {
    left = mid + 1;
}
```

If the middle value is **greater than** the target, the target must be in the **left half**:
```java
else {
    right = mid - 1;
}
```

---

### ✅ Final Step: Full Code

Now put it all together:
```java
public int binarySearch(int[] arr, int target) {
    int left = 0, right = arr.length - 1;
    while (left <= right) {
        int mid = (left + right) / 2;

        if (arr[mid] == target) {
            return mid; // Target found
        } else if (arr[mid] < target) {
            left = mid + 1; // Search right half
        } else {
            right = mid - 1; // Search left half
        }
    }
    return -1; // Target not found
}
```

Let me know if you'd like to see a version that avoids integer overflow or works recursively!