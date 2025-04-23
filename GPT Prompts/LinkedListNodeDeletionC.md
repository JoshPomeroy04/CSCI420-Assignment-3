# Zero-shot Prompting

## Input
    Implement node deletion by value:

    struct Node {
        int data ;
        struct Node * next ;
    };

    void deleteNode ( struct Node ** head , int key ) {
        // TODO : Implement node deletion
    } 

## Output
Sure! Let's walk through how to implement the `deleteNode` function to delete a node by value (`key`) in a singly linked list in C.

---

### ✅ Goal:
Given a pointer to the head of a linked list and an integer `key`, delete the **first node** with `data == key`.

---

### ✅ Steps:
1. Handle the case where the head node contains the key.
2. Traverse the list to find the node **just before** the one to delete.
3. Update the `next` pointer to skip the target node.
4. Free the memory of the deleted node.

---

### ✅ Implementation:

```c
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

void deleteNode(struct Node **head, int key) {
    struct Node *temp = *head;
    struct Node *prev = NULL;

    // Case 1: The head node itself holds the key
    if (temp != NULL && temp->data == key) {
        *head = temp->next;  // Move head to next node
        free(temp);          // Free old head
        return;
    }

    // Case 2: Search for the key
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    // If key was not present in the list
    if (temp == NULL) return;

    // Unlink the node from the list
    prev->next = temp->next;
    free(temp);
}
```

---

### 📝 Example Usage:

```c
// Assuming a helper function exists to create and print the list
deleteNode(&head, 42); // Deletes the first node with value 42
```

Let me know if you'd like the full list creation and testing code too!


# Two-shot Prompting

## Input
    Original List: 3 2 5 7
    List after deleting 3: 2 5 7

    Original List: 3 2 5 7
    List after deleting 5: 3 2 7

    struct Node {
        int data ;
        struct Node * next ;
    };

    void deleteNode ( struct Node ** head , int key ) {
        // TODO : Implement node deletion
    }

## Output
Here's the correct implementation of the `deleteNode` function that handles deletion of the first node with the given value (`key`) from a singly linked list:

---

### ✅ C Implementation of `deleteNode`:

```c
#include <stdlib.h>

struct Node {
    int data;
    struct Node *next;
};

void deleteNode(struct Node **head, int key) {
    struct Node *temp = *head;
    struct Node *prev = NULL;

    // Case 1: Head node holds the key
    if (temp != NULL && temp->data == key) {
        *head = temp->next;  // Move head to the next node
        free(temp);          // Free old head
        return;
    }

    // Case 2: Traverse the list to find the key
    while (temp != NULL && temp->data != key) {
        prev = temp;
        temp = temp->next;
    }

    // If key is not found, do nothing
    if (temp == NULL) return;

    // Unlink the node and free memory
    prev->next = temp->next;
    free(temp);
}
```

---

### ✅ Example:

For input list: `3 -> 2 -> 5 -> 7`:

- Calling `deleteNode(&head, 3);` results in `2 -> 5 -> 7`.
- Calling `deleteNode(&head, 5);` results in `3 -> 2 -> 7`.

---

Let me know if you want the helper functions like `insertNode` or `printList` to test this out.