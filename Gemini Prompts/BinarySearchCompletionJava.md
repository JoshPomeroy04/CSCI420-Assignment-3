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
```java
public int binarySearch ( int [] arr , int target ) {
    int left = 0 , right = arr . length - 1;
    while ( left <= right ) {
        int mid = ( left + right ) / 2;
        if ( arr [ mid ] == target ) {
            return mid; // Target found at index mid
        } else if ( arr [ mid ] < target ) {
            left = mid + 1; // Target is in the right half
        } else {
            right = mid - 1; // Target is in the left half
        }
    }
    return -1; // Target not found in the array
}
```

In this implementation:

1.  We initialize `left` to the start index (0) and `right` to the end index (`arr.length - 1`) of the array.
2.  The `while` loop continues as long as the `left` index is less than or equal to the `right` index, meaning there's still a valid search space.
3.  Inside the loop, we calculate the middle index `mid`.
4.  We then compare the element at `arr[mid]` with the `target`:
    * If they are equal, we've found the target and return `mid`.
    * If `arr[mid]` is less than the `target`, it means the target (if present) must be in the right half of the array, so we update `left` to `mid + 1`.
    * If `arr[mid]` is greater than the `target`, the target (if present) must be in the left half, so we update `right` to `mid - 1`.
5.  If the loop finishes without finding the target (i.e., `left` becomes greater than `right`), we return `-1` to indicate that the target is not present in the array.


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
Okay, let's complete the binary search implementation step by step:

**Step 1: Initialize the search space**

You've already done this part. We start by defining the boundaries of our search within the sorted array:

```java
public int binarySearch ( int [] arr , int target ) {
    int left = 0 , right = arr . length - 1;
    // 'left' points to the beginning of the current search space.
    // 'right' points to the end of the current search space.
    while ( left <= right ) {
        int mid = ( left + right ) / 2;
        // TODO : Compare and adjust bounds
    }
    return -1;
}
```

**Step 2: Calculate the middle index**

Inside the `while` loop, we need to find the middle index of the current search space. This is where we'll check for the target value:

```java
public int binarySearch ( int [] arr , int target ) {
    int left = 0 , right = arr . length - 1;
    while ( left <= right ) {
        int mid = ( left + right ) / 2;
        // 'mid' is the index of the middle element in the current search space.
        // TODO : Compare and adjust bounds
    }
    return -1;
}
```

**Step 3: Compare the middle element with the target**

Now, we compare the value at the middle index (`arr[mid]`) with the `target` value. There are three possible outcomes:

* **The middle element is equal to the target:** We've found the target!
* **The middle element is less than the target:** The target (if it exists) must be in the right half of the current search space.
* **The middle element is greater than the target:** The target (if it exists) must be in the left half of the current search space.

Let's add the `if-else if-else` block to handle these comparisons:

```java
public int binarySearch ( int [] arr , int target ) {
    int left = 0 , right = arr . length - 1;
    while ( left <= right ) {
        int mid = ( left + right ) / 2;
        if ( arr [ mid ] == target ) {
            return mid; // Target found at the middle index.
        } else if ( arr [ mid ] < target ) {
            // The target is greater, so we narrow our search to the right half.
            // TODO : Adjust 'left' bound.
        } else { // arr[mid] > target
            // The target is smaller, so we narrow our search to the left half.
            // TODO : Adjust 'right' bound.
        }
    }
    return -1;
}
```

**Step 4: Adjust the search space boundaries**

Based on the comparison in the previous step, we need to adjust the `left` or `right` boundaries to narrow down our search space:

* If `arr[mid] < target`, we know the target cannot be in the left half (including `mid`), so we update `left` to `mid + 1`.
* If `arr[mid] > target`, we know the target cannot be in the right half (including `mid`), so we update `right` to `mid - 1`.

Let's complete the `if-else if-else` block with these adjustments:

```java
public int binarySearch ( int [] arr , int target ) {
    int left = 0 , right = arr . length - 1;
    while ( left <= right ) {
        int mid = ( left + right ) / 2;
        if ( arr [ mid ] == target ) {
            return mid; // Target found at the middle index.
        } else if ( arr [ mid ] < target ) {
            left = mid + 1; // Search in the right half.
        } else { // arr[mid] > target
            right = mid - 1; // Search in the left half.
        }
    }
    return -1;
}
```

**Step 5: Handle the case where the target is not found**

If the `while` loop finishes without finding the target (meaning `left` becomes greater than `right`), it indicates that the target is not present in the array. In this case, the function should return `-1`, which you have already included at the end of the function.

And there you have it! The complete step-by-step implementation of the binary search algorithm.