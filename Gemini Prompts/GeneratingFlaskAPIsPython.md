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
```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<username>')
def greet(username):
    greeting = {"message": f"Hello, {username}! Welcome!"}
    return jsonify(greeting)

if __name__ == '__main__':
    app.run(debug=True)
```

Now, if you run this Flask application and navigate to a URL like `http://127.0.0.1:5000/greet/Alice` in your web browser or using a tool like `curl`, you will receive the following JSON response:

```json
{
  "message": "Hello, Alice! Welcome!"
}
```

The `jsonify()` function from Flask automatically converts the Python dictionary into a JSON response with the correct `Content-Type` header.


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
Alright, let's break down how to complete that Flask endpoint step by step.

**Step 1: Import necessary modules**

You've already got this part covered in your code:

```python
from flask import Flask, jsonify
```

This line imports the `Flask` class, which you'll use to create your application instance, and the `jsonify` function, which is essential for converting Python dictionaries into JSON responses.

**Step 2: Create a Flask application instance**

Again, you've already done this:

```python
app = Flask(__name__)
```

This line creates an instance of the Flask application. The `__name__` argument is a Python special variable that helps Flask determine the root path of your application.

**Step 3: Define the route and associated view function**

You have the route defined using the `@app.route()` decorator:

```python
@app.route('/greet/<username>')
def greet(username):
    # TODO : Return a JSON greeting
    pass
```

* `@app.route('/greet/<username>')`: This decorator tells Flask what URL should trigger the `greet` function.
    * `/greet/`: This is the base path for your endpoint.
    * `<username>`: This is a dynamic part of the URL. Flask will capture whatever the user types in place of `<username>` and pass it as an argument to your `greet` function.

* `def greet(username):`: This defines the view function that will be executed when a user visits the `/greet/<username>` URL. The `username` parameter will hold the value captured from the URL.

**Step 4: Implement the logic to return a JSON greeting**

Inside the `greet` function, you need to create a Python dictionary that represents the greeting and then convert it to a JSON response using `jsonify()`.

```python
@app.route('/greet/<username>')
def greet(username):
    greeting = {"message": f"Hello, {username}! Welcome to Williamsburg!"}
    return jsonify(greeting)
```

* `greeting = {"message": f"Hello, {username}! Welcome to Williamsburg!"}`: This line creates a Python dictionary. The key `"message"` holds a greeting string that includes the `username` captured from the URL. Since we're in Williamsburg, Virginia, I've personalized the welcome a bit!
* `return jsonify(greeting)`: This line uses the `jsonify()` function to convert the `greeting` dictionary into a JSON response. Flask will automatically set the correct `Content-Type` header (`application/json`) for the response.

**Step 5: Add a conditional block to run the app**

It's good practice to include the following block at the end of your script:

```python
if __name__ == '__main__':
    app.run(debug=True)
```

* `if __name__ == '__main__':`: This ensures that the following code only runs when the script is executed directly (not when it's imported as a module).
* `app.run(debug=True)`: This starts the Flask development server. The `debug=True` option is helpful during development as it provides automatic reloading upon code changes and more detailed error messages.

**Putting it all together:**

Here's the complete code for your `app.py` file:

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/greet/<username>')
def greet(username):
    greeting = {"message": f"Hello, {username}! Welcome to Williamsburg!"}
    return jsonify(greeting)

if __name__ == '__main__':
    app.run(debug=True)
```

**To run this application:**

1.  Save the code as a Python file (e.g., `app.py`).
2.  Open your terminal or command prompt.
3.  Navigate to the directory where you saved the file.
4.  Run the command: `python app.py`
5.  Open your web browser or use a tool like `curl` to access URLs like `http://127.0.0.1:5000/greet/John` or `http://127.0.0.1:5000/greet/Jane`. You should see the JSON greeting in the response.