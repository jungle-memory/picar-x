# Bare Flask App

This project folder contains the minimal code needed to run a Flask app.  

###### https://www.youtube.com/embed/OKavgGmuDPo

## [What is Flask?](what-is-flask)

Flask is a Python micro web framework for making web applications. 

It includes the basic functionality needed to create and manage a website. 

The best part about Flask is that it is easy to learn and use.

## [What is Flask used for?](#what-is-flask-used-for) 

Flask is used for making servers and fullstack web applications. 

While primarily thought of for making servers and micro-services, Flask comes with built-in software for making frontends, too.  

It can be used to build a blog, an API, or even an e-commerce platform. 

Flask is a great option for web applications that incorporate machine learning, artificial intelligence, data science, the Internet of Things, and hardware like the Raspberry Pi. 

Flask is easy to use with those technologies because the Python ecosystem has lots of packages, documentation, and tutorials for them.  

## [Does Flask require special software?](#does-flask-require-special-software)

Flask does not require any specific tools or libraries in order to use it. 

For instance, it does not have a database abstraction layer. So you can easily connect your Flask application to MongoDB, SQL, and virtually any other storage solution. 

Flask also does not come with form validation. You can implement your own form validation solutions or something from a third-party.

You will, however, need Python installed on your computer, a code editor like Visual Studio code, and the Flask package installed in your project.  

See the [the Flask setup explanation to learn more](https://thacash.com/flask/code-samples/getting-started/0_flask-setup).  

![](https://app.thacash.com/wp-content/uploads/2022/02/flask-app-example.png)

Other web frameworks, like Django, come with more pre-built requirements and therefore are not as flexible.   

## [How do you run a Flask app?](#how-do-you-run-a-flask-app)  

You can run a Flask app on your computer. You can have one up and running in 2 minutes.

Want to do it now? 

The accompanying `.py` file has code for making a basic Flask server.

Here is how to run the sample code in the accompanying folder:

- clone or download this folder
- create a virtual environment
- install Flask  
- freeze the dependencies to the requirements.txt file. 
- run the app.py file   

## [Flask server example](flask-server-example)

Code example with explanations are in the app.py file located in this folder and below.

Here is a bare flask app:


```python
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World"


@app.route("/stocks")
def stocks():
    return "Hello Stocks"


if __name__ == "__main__":
    app.run(host="localhost", port=2000, debug=True, use_reloader=True)
```

Here is the same code but with comments that explain the code:

```python
# import Flask
from flask import Flask


# Create an instance of a Flask server
# Flask has the basic functionality we want for the server
# __name__ is a variable representing the module (folder) that you 
# call Flask inside of
app = Flask(__name__)


# The following is from: 
# https://blog.miguelgrinberg.com/post/why-do-we-pass-name-to-the-flask-class

# Python sets the __name__ variable to the module name, so the 
# value of this variable depends on the Python source 
# file in which you use it.

# For example, in a module named test.py located in the  
# top-level directory of the application, the value of __name__ is
# test.
# If the test.py module is located inside a Python package called  
# my_package, then the value of __name__ is my_package.test.


# Exceptions regarding the value of __name__:
## 1. Inside __init__.py package constructor module, the value  
## of __name__ is the package name, without __init__.
## For example, in my_package/__init__.py, the value of __name__  
## is just my_package.
## 2. In the main module of the application (the file you run the 
## Python interpreter on) the value of __name__ has the special 
## value of __main__.


# Create a route
# This route corresponds to the host on which you run the server
# You see below the server will run on port 2000, so this route 
# is http://localhost:2000/
@app.route("/")
def home():
    return "Hello World"


# Create annother route
# This route corresponds to the host + "/stocks" 
# Below you see the server will run on port 2000, so this route is 
# http://localhost:2000/stocks
@app.route("/stocks")
def stocks():
    return "Hello Stocks"


# The next lines of code are what run the server
# The if statment means the server only runs from the main (root) 
# folder in your project because it checks if __name__ == "__main__"
# It runs on localhost:2000, so you can open that in your browser  


if __name__ == "__main__":
    app.run(host="localhost", port=2000, debug=True, use_reloader=True)

# To run the file, open a terminal session in your root folder
# Type python3 app.py and hit enter


# After running the server:
# Open the browser and go to http://localhost:2000/
# The browser should say "Hello World"
# Then open the browser and go to http://localhost:2000/stocks
# The browser should say "Hello Stocks"
```
## [What are Python packages?](#what-are-python-packages)

You are learning about packages now because you will work with packages in every Flask application. In fact, Flask is a Python package.

To get the code sample above working, you need to install Flask.

```python
pip3 install Flask
```

You also need to import it into your code.

```python
from flask import Flask
```

Python packages, like Flask, allow for easy modularization and code reuse among your applications and between the development community.    

When you need to integrate new functionality, it can be faster and easier to use third-party Python packages than build it yourself. 

For example, in the code in this sample, instead of writing all the basic functionality that a server needs, you just use Flask instead.  

Python is much more than just a popular programming language. It is a development ecosystem.  

What makes it such a powerful ecosystem is its robust collection of third-party packages you can import into your project.  

Python packages are small parts of code developed by other developers that you can use in your applications. 

Packages are typically distributed through the Python Package Index, commonly referred to as PyPI. 

Most packages are free and have documentation that provide a clear purpose for what the package can do and how to use it.

You could write a Python package and distribute it through PyPI if you want.   

Packages have different functions and purposes from one another, but they all share one goal: to make it easier for the developer community to write better and more efficient programs.  

A package might contain just a single function or class, but packages are commonly used in applications because they allow developers to concentrate on the app's logic rather than reinventing the wheel. 

In other words, packages save you the time of having to write code that other people have already written and perfected.  

When you install a package in your virtual environment, it automatically downloads from the internet and is installed in the lib folder inside your virtual environment.

Another example of a Python package is NumPy. It is a package that contains pre-built code that is commonly needed in applications used for scientific computing. You can download it just like you did for Flask and use it to help with scientific computing.  

## [What is an object in Python?](#what-is-an-object-in-python)

You are learning about objects now because you are using one in the code sample. 

In the code below, app is the object.

```
app = Flask(__name__)
```

You created the object using the Flask class and an argument called `__name__`.

Before creating the object, you import Flask from flask. 

When you do that, you are importing a class named Flask from the flask package. 

Uppercase 'f' Flask is a class whose code lives in the flask package, and lowercase 'f' flask is the entire flask package.

A class is a blueprint for making objects. It can have its own functionality, data, and state. State is like a memory or status.  

When you use the class, you create a specific copy of the class. Each copy is called an object and is a bundle of distinct functionality and data.   

It is a confusing topic, which is why right now it is only important that you get exposure to it.

Buy maybe an analogy will help. 

A class is like a blueprint for making a house. 

Like you use the house blueprint to build houses that all have some basic features in common, a class is used to create objects that all have some basic functionality or data in common.

The same class can be associated with different objects. 

You can build mulitple houses using the same blueprint, each house being a specific implementation of that blueprint.

Similarly, an object is a specific instance that results from using the class.  

Not all objects from the same class are identical.

Like you can customize each house to have some features that are different than the others from the same blueprint, you can customize the data and state of an object created by the class. 

For now, just know that app is an object that has all the functionality bundled in the Flask app. That might help when you are researching what app can you. You should research about the functionality and data that comes with the Flask class.  

## [What is a Flask route?](#what-is-a-Flask-route)

You are learning about Python functions now because you are using them in the code above. 

```python
@app.route("/")

@app.route("/stocks")
```

As with many of the other topics so far, the purpose about learning about routes now is not to learn all the details.  

Instead, the current goal is to know that they exist and to start learning enough so that later you will be able to research and problem-solving on your own as a Flask developer.

## [What is a function in Python?](#what-is-a-function-in-python) 

You are learning about Flask routes now because you are using two in the code above. Plus, you will use them in every Flask project. Every route is attached to a function, your route functions will call other functions, and the third-party packages you use will have functions that you call.

In the code above, two function definitions that you wrote are:

```python
def home():
    return "Hello World"

def home():
    return "Hello World"
```

You call those functions by visiting the routes associated with them.  

You can have functions that are not associated with routes. You call them using the name, plus parenthesis and any arguments.

For instance, here is a function definition that takes one argument, adds 10 to it, and returns the result.

```python
def addTen(input_number):
    sum = input_number + 10
    return sum
```

You can call that function definition like this.

```python
addTen(8)
```

The function adds 10 + 8 and returns the result.

Function definitions can live inside objects. 

You call one of those in the code above, run is the function that you call whose definition is in the app object.  

This is just the beginning of learning about functions. There is so much more to know.  





