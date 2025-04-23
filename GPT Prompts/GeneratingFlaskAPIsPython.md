# Zero-shot Prompting

## Input 
    Create a ‘/greet/<username>‘ endpoint that returns a JSON greeting:
            from flask import Flask , jsonify
            app = Flask ( __name__ )
            @app . route (’/ greet / < username >’)
            def greet ( username ) :
                # TODO : Return a JSON greeting
                pass


## Output 
Here’s how you can complete the Flask endpoint to return a JSON greeting:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<username>')
def greet(username):
    return jsonify({'message': f'Hello, {username}!'})

if __name__ == '__main__':
    app.run(debug=True)
```

### How it works:
- The route `/greet/<username>` captures a dynamic `username` from the URL.
- `jsonify` wraps the greeting message in a JSON response.
- When you visit `http://localhost:5000/greet/Josh`, you'll get:
  ```json
  {"message": "Hello, Josh!"}
  ```

Let me know if you want to include additional info like the current time or a custom message!

# Chain-of-Thoughts Prompting

## Input 
    Step by step, create a ‘/greet/<username>‘ endpoint that returns a JSON greeting:
            from flask import Flask , jsonify
            app = Flask ( __name__ )
            @app . route (’/ greet / < username >’)
            def greet ( username ) :
                # TODO : Return a JSON greeting
                pass
    
## Output 
Sure! Here's how you can create the `/greet/<username>` endpoint **step by step**:

---

### ✅ **Step 1: Import Required Modules**
Start by importing `Flask` and `jsonify` from the `flask` package.

```python
from flask import Flask, jsonify
```

---

### ✅ **Step 2: Create a Flask App Instance**
Initialize the Flask application.

```python
app = Flask(__name__)
```

---

### ✅ **Step 3: Define the Route with a Dynamic URL Parameter**
Create a route `/greet/<username>` using the `@app.route()` decorator. This means any string provided after `/greet/` in the URL will be captured as `username`.

```python
@app.route('/greet/<username>')
def greet(username):
    # TODO: Return a JSON greeting
    pass
```

---

### ✅ **Step 4: Return a JSON Response**
Inside the `greet()` function, use `jsonify()` to return a dictionary with a greeting message.

```python
@app.route('/greet/<username>')
def greet(username):
    return jsonify({'message': f'Hello, {username}!'})
```

---

### ✅ **Step 5: Run the App**
Add this block to make sure the app runs when you execute the script.

```python
if __name__ == '__main__':
    app.run(debug=True)
```

---

### ✅ **Final Code:**

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<username>')
def greet(username):
    return jsonify({'message': f'Hello, {username}!'})

if __name__ == '__main__':
    app.run(debug=True)
```

---

Now if you go to `http://localhost:5000/greet/Josh`, the server will return:

```json
{"message": "Hello, Josh!"}
```

Let me know if you'd like to personalize it more or add error handling!