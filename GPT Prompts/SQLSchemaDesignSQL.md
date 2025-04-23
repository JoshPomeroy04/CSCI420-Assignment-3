# Zero-shot Prompting

## Input 
    Write the schema for a review app with users, books, and reviews:

    -- TODO : Design schema with appropriate keys and constraints
    -- Tables : users (id , name ), books (id , title ), reviews (id , user_id , book_id , rating )

## Output
Here's a well-structured SQL schema for a review app involving `users`, `books`, and `reviews` tables, complete with primary and foreign keys, appropriate constraints, and indexing for good relational integrity and performance:

```sql
-- Users Table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- Books Table
CREATE TABLE books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL
);

-- Reviews Table
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),

    -- Foreign Keys
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,

    -- Unique constraint to prevent duplicate reviews by same user on same book
    UNIQUE (user_id, book_id)
);
```

### Notes:
- **`SERIAL`** is used for auto-incrementing primary keys.
- **`CHECK`** constraint ensures `rating` is between 1 and 5.
- **`UNIQUE (user_id, book_id)`** ensures that a user can only leave one review per book.
- **`ON DELETE CASCADE`** ensures that if a user or book is deleted, their reviews are also removed.

Let me know if you want timestamps, support for review text, or more advanced features like likes on reviews.


# Chain-of-Thoughts Prompting

## Input 
    Step by step, write the schema for a review app with users, books, and reviews:

    -- TODO : Design schema with appropriate keys and constraints
    -- Tables : users (id , name ), books (id , title ), reviews (id , user_id , book_id , rating )

## Output
Sure! Let’s build the schema for your review app step by step, following proper database design practices.

---

### 🧩 Step 1: Create the `users` table
We'll start by creating a table for users with a unique ID and a name.

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,      -- Unique identifier for each user
    name VARCHAR(100) NOT NULL  -- Name of the user, required
);
```

---

### 📚 Step 2: Create the `books` table
Next, we define the books table, storing each book's unique ID and title.

```sql
CREATE TABLE books (
    id SERIAL PRIMARY KEY,       -- Unique identifier for each book
    title VARCHAR(255) NOT NULL  -- Title of the book, required
);
```

---

### ✍️ Step 3: Create the `reviews` table
Now we define the reviews table, which connects users and books with a rating.

```sql
CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,       -- Unique identifier for each review
    user_id INTEGER NOT NULL,    -- References the user who wrote the review
    book_id INTEGER NOT NULL,    -- References the book being reviewed
    rating INTEGER NOT NULL CHECK (rating >= 1 AND rating <= 5),  -- Must be 1-5

    -- Foreign keys to maintain referential integrity
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE,
    FOREIGN KEY (book_id) REFERENCES books(id) ON DELETE CASCADE,

    -- Prevents a user from reviewing the same book more than once
    UNIQUE (user_id, book_id)
);
```

---

### ✅ Summary of Constraints:
- `PRIMARY KEY` ensures uniqueness of each row.
- `FOREIGN KEY` ensures valid references between tables.
- `CHECK` ensures ratings are between 1 and 5.
- `UNIQUE (user_id, book_id)` enforces only one review per user per book.
- `ON DELETE CASCADE` automatically removes related reviews if a user or book is deleted.

Let me know if you'd like to add more features like review comments, timestamps, or user emails!