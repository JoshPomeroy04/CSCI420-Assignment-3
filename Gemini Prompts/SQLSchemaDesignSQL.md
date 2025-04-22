# Zero-shot Prompting

## Input 
    Write the schema for a review app with users, books, and reviews:

    -- TODO : Design schema with appropriate keys and constraints
    -- Tables : users (id , name ), books (id , title ), reviews (id , user_id , book_id , rating )

## Output
```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);

CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    CHECK (rating >= 1 AND rating <= 5)
);
```

This schema defines three tables:

* **users**: Stores information about the users of the app.
    * `id`: Unique identifier for each user (primary key, automatically incrementing).
    * `name`: The name of the user (cannot be empty).
* **books**: Stores information about the books.
    * `id`: Unique identifier for each book (primary key, automatically incrementing).
    * `title`: The title of the book (cannot be empty).
* **reviews**: Stores the reviews given by users for specific books.
    * `id`: Unique identifier for each review (primary key, automatically incrementing).
    * `user_id`: Foreign key referencing the `id` from the `users` table, indicating who wrote the review (cannot be empty).
    * `book_id`: Foreign key referencing the `id` from the `books` table, indicating which book is being reviewed (cannot be empty).
    * `rating`: The rating given by the user for the book (cannot be empty, and is constrained to be between 1 and 5 inclusive).

The `FOREIGN KEY` constraints ensure data integrity by linking reviews to existing users and books. The `CHECK` constraint on the `rating` column enforces a valid rating range.


# Chain-of-Thoughts Prompting

## Input 
    Step by step, write the schema for a review app with users, books, and reviews:

    -- TODO : Design schema with appropriate keys and constraints
    -- Tables : users (id , name ), books (id , title ), reviews (id , user_id , book_id , rating )

## Output
Okay, let's build this schema step by step.

**Step 1: Define the `users` table.**

This table will store information about the users of our review app. Each user will have a unique identifier and a name.

```sql
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);
```

* `CREATE TABLE users`: This statement initiates the creation of a new table named `users`.
* `id INTEGER PRIMARY KEY AUTOINCREMENT`: This defines a column named `id`.
    * `INTEGER`: Specifies that the data type of this column will be an integer.
    * `PRIMARY KEY`: Indicates that this column will serve as the unique identifier for each row in the `users` table. This ensures that each user has a distinct `id`.
    * `AUTOINCREMENT`: This keyword (common in SQLite and some other SQL databases) automatically assigns the next available integer as the `id` for each new user added to the table.
* `name TEXT NOT NULL`: This defines a column named `name` to store the user's name.
    * `TEXT`: Specifies that the data type of this column will be text (variable-length string).
    * `NOT NULL`: This constraint ensures that the `name` field cannot be left empty when a new user is added. Every user must have a name.

**Step 2: Define the `books` table.**

This table will store information about the books that users can review. Each book will have a unique identifier and a title.

```sql
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
);
```

* `CREATE TABLE books`: This statement initiates the creation of a new table named `books`.
* `id INTEGER PRIMARY KEY AUTOINCREMENT`: Similar to the `users` table, this defines a unique, automatically incrementing integer identifier for each book.
* `title TEXT NOT NULL`: This defines a column named `title` to store the book's title, ensuring that every book has a title.

**Step 3: Define the `reviews` table.**

This table will store the actual reviews written by users for specific books. It will link users to books and store their rating.

```sql
CREATE TABLE reviews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    rating INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (book_id) REFERENCES books(id),
    CHECK (rating >= 1 AND rating <= 5)
);
```

* `CREATE TABLE reviews`: This statement initiates the creation of a new table named `reviews`.
* `id INTEGER PRIMARY KEY AUTOINCREMENT`: This defines a unique, automatically incrementing integer identifier for each review.
* `user_id INTEGER NOT NULL`: This column will store the `id` of the user who wrote the review.
    * `INTEGER`: Specifies the data type as an integer.
    * `NOT NULL`: Ensures that every review is associated with a user.
* `book_id INTEGER NOT NULL`: This column will store the `id` of the book being reviewed.
    * `INTEGER`: Specifies the data type as an integer.
    * `NOT NULL`: Ensures that every review is associated with a book.
* `rating INTEGER NOT NULL`: This column will store the rating given by the user.
    * `INTEGER`: Specifies the data type as an integer.
    * `NOT NULL`: Ensures that every review has a rating.
* `FOREIGN KEY (user_id) REFERENCES users(id)`: This is a foreign key constraint.
    * `FOREIGN KEY (user_id)`: Specifies that the `user_id` column in the `reviews` table is a foreign key.
    * `REFERENCES users(id)`: Indicates that the values in the `user_id` column must match existing values in the `id` column of the `users` table. This enforces referential integrity, ensuring that a review is always linked to a valid user.
* `FOREIGN KEY (book_id) REFERENCES books(id)`: This is another foreign key constraint, similar to the one above.
    * `FOREIGN KEY (book_id)`: Specifies that the `book_id` column is a foreign key.
    * `REFERENCES books(id)`: Indicates that the values in the `book_id` column must match existing values in the `id` column of the `books` table, ensuring that a review is always linked to a valid book.
* `CHECK (rating >= 1 AND rating <= 5)`: This is a check constraint.
    * `CHECK (...)`: Defines a condition that must be true for any new or updated row in the `reviews` table.
    * `rating >= 1 AND rating <= 5`: This specific condition ensures that the `rating` value is always within the valid range of 1 to 5 (inclusive).

This step-by-step breakdown explains the SQL code to create the schema with appropriate keys and constraints for your review app.