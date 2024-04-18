# Web Development with Python: Advanced Python

# 3.4.1 Flask:

# Flask is a lightweight web application framework for Python. It provides tools, libraries, and patterns to help you build web applications quickly and easily.

# Example: Creating a Simple Flask App
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
