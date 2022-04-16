# Flask Setup

This file contains quickstart instructions to get you building in Flask even if you have no experience with Flask, Python, or coding.  

## Flask Quickstart 

1. [Getting Started](#getting-started)
2. [Install Python](#install-python)
3. [Install Visual Studio Code](#install-visual-studio-code)
4. [Create Virtual Environment](#create-virtual-environment)
5. [Activate Virtual Environment](#activate-virtual-environment)
6. [Install Flask](#install-flask)
7. [Create App File](#create-app-file)
8. [Run App File](#run-app-file)
9. [Next lesson](#next-lesson)  

Our focus is on making things. Yes, we want to understand how things work, but our priority is first to get things working.  

It is hard to just start making things without any knowledge. To help with this, we provide you step-by-step instructions with explanations so that you can get things working.  

Our instructions not only get things working, they also start to teach you how things work and how to become an independent developer. Learn techniques and gain knowledge that give you the skills to figure out how things work on your own.  

You do not need to learn the materials below as if you are studying for a test. Instead, just see if you can follow the instructions and get things working. 

## [Getting Started](#getting-started)

Making software with Flask requires knowing how to setup and maintain your Python programming environment. Making software is so much more than just knowing what code to write.  

You should know how to use the terminal, how to install and work with code other people wrote, how to setup and activate your virtual environment, and of course so much more. 

This may sound intimidating at first, but it is actually a very fun part of programming.  

By following the steps below, you will setup your coding environment and make your first Flask web application.  

You will use the terminal, install software, and learn two ways to run your Python code. 

## [Install Python](#install-python)

You need to have Python installed on your computer. Some computers have Python pre-installed and others do not.  

Even if a computer has Python pre-installed, Python has versions 2 and 3 available for use, so you want to make sure you know which version you have. 

Check whether you have Python installed and which versions by using the terminal. Check for both Python 2 and Python 3. 

Open up a terminal session on your computer. If you do not know how to do that, search your computer for the word terminal and you should see it. 

You use the terminal to interact with the folders, files, and software on your computer without using the graphical user interface. The terminal is also called the command lines or console.

Your terminal should look something like this:

![](https://app.thacash.com/wp-content/uploads/2022/02/terminal-example.png)

In the terminal session, enter `python3 --version` to check whether you have Python 3 installed and which version. 

```python
python3 --version
```

You also should check whether you have Python 2 installed. To do that, run `python --version`. 

```python
python --version
```

If you have that Python version installed, the terminal will respond with the version number.


```python
Python 3.7.7
```

Or . . .

```python
Python 2.7.16
```

You do not need both versions installed. You will probably work with one or the other.  

As for which one you should use, you should work with Python 3 unless you are working on a project that is already written in Python 2.  

If you do not have the Python version that you want, install it. Visit the [Python downloads](https://www.python.org/downloads/) page.  

Find the page for your operating system. Choose the version you want to download and follow the installation instructions.  

When installation is complete, check again whether Python is installed.  

If you have Python installed, test it out! 

Open a Python session in the terminal. To do that, open the terminal, type `python3`, and hit `Enter`. 

The `python3` command starts a session using Python 3. 

We will use Python 3, but if you are using Python 2, you can still follow along. Just use the `python` command instead of `python3`. The `python` command starts a session using Python 2.  

The terminal should respond with the Python version, some additional information, and then `>>>`. Next to the `>>>`, you can write Python code.  

```python
Python 3.7.7 (default, Mar 10 2020, 15:43:03) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

Start by getting Python to print something to the terminal.  
 
If you want Python to print text to the terminal, you need to tell Python that the text is a string. A string is a type that Python uses for storing data. You will learn later about data types. To learn more now, you can visit this [overview page about Python datatypes](https://www.w3schools.com/python/python_datatypes.asp).  

To do that, wrap in single `' '` or double `" "` quotes what you type into the terminal, and Python will know that what you typed is a string. The terminal should print what you typed.  

In your terminal session, next to the `>>>`, type `'Coding with Python'` (be sure to include the quotes) and hit `Enter`.  

```python
>>> 'Coding with Python'

'Coding with Python'
```

Try something else.  

Below the print, you should see another `>>>`. Next to it, type `Coding with Python`, and this time do not wrap it in quotes. Hit `Enter`.  

The terminal should print an error message.  

```python
>>> Coding with Python

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Coding with Python' is not defined
```

What?!  

You receive this error because you need to wrap text in single `' '` or double `" "` quotes.  

Without the quotes, Python does not know what it is that you entered because Python thinks the text is a variable, looks for it in the memory, does not find it, and then tells you that the text is undefined.  

Strings are one of several Python built-in data types. Numbers are another data type.  

Try printing a number. You should see another `>>>` at the bottom of your Python session in the terminal.  

Next to it, type a number, like `8`. Do not wrap it in quotes. Hit `Enter`.  

The terminal does not return an error!  

It prints the number.   

Python recognizes the number you entered as number data type. Numbers are not wrapped in quotes.  

```python
>>> 8

8
```

Note that if you wrap the 8 in quotes, it is a string data type even though the character inside the string is a number.  

To exit the Python session in your terminal, type `exit()` and hit `Enter`. 

The terminal should show the path to your present working directory, which is the folder on your computer to which the terminal is pointing.  

## [Install Visual Studio Code](#install-visual-studio-code)  

Writing Python code in your terminal like you did in the previous step is an okay way to practice writing Python code.  

But what is better is using an integrated development environment (IDE).  

Like Microsoft Word is software for writing word documents, an IDE is software for writing code.    

One of the most popular IDEs is Microsoft's Visual Studio Code.  

It is a free code editor that you can use with Windows, Linux and macOS.    

VS Code has built-in tools to help you write code. 

For instance, it has tools that help with debugging, highlight syntax, provide intelligent code auto-completion, suggest code snippets, format your code, and embed Git. 

You can also install extensions that add additional functionality.

[Install VS Code](https://docs.microsoft.com/en-us/visualstudio/install/install-visual-studio?view=vs-2019) by visiting the Microsoft installation page. 

Follow the instructions for downloading the correct version to your operating system.  

Next, create an empty folder somewhere on your computer. 

Name it `flask_getting_started`. 

In VS Code, choose `File --> Open` and open the `flask_getting_started` folder. 

On the lefthand side of your VS Code, you should see a pane that lists the `flask_getting_started` folder. 

In VS Code, right click on `flask_getting_started` and choose `New File`.  

Name the new file app.py. You can name it whatever you want, but naming it this is one popular convention and what we will use generally in our code samples.   

At the top of your app.py file, type `print("Getting started with Flask").` 

In VS Code, choose `File --> Terminal`.  

This should open up a terminal session inside your VS Code.  

If you read the line that appears in the terminal when you open it, you should see that it is located within your `flask_getting_started` project folder. 

If not, in the terminal, type `cd`, then spacebar, and then drag your `flask_getting_started` folder to the terminal. This should result in a path to your `flask_getting_started` folder appearing in the terminal. Then hit enter.

Once your terminal points to your `flask_getting_started` project folder, run your Python file.  

To run the Python file, in the terminal type `python3 app.py` and hit Enter. 

It should print to the terminal the message you put in the print statement in your app.py file --> `"Getting started with Flask"`.

If that worked, then your project setup is correct!

## [Create Virtual Environment](#create-virtual-environment)

After confirming that your project setup is correct, create a virtual environment. 

A virtual environment is like a container for your project. In this container you store all the third-party software that your project depends upon.  

By creating a virtual environment, you keep the project's dependencies separate from the dependencies of your other projects on the same computer. 

For instance, using virtual environments allows you to have one Flask project that uses Flask version 1.1.2 and Python 3.7 and another Flask project that uses Flask version 1.0 and Python 3.6.4. 

You can run them from the same computer without having to uninstall and reinstall the packages when switching between projects. 

As you learn more about below, you also can share and store your code more efficiently by saving a list of the packages in your virtual environment. 

Someone can download your code and have it working on their machine by creating a virtual environment and installing the list of dependencies. The opposite is true true. You could download someone else's code, create a virtual environment, and install the dependencies to have their code up and running on your computer.  

Because of its role as a partition between projects, setting up a virtual environment should be part of the initial setup of every Flask application because all of them will require dependencies.  

Confirm the terminal is in the root level of your project folder. The root level is the outer-most level of your Flask project folder.  

Look at your project folder and notice that it does not have an venv folder. 

As shown below, enter the command in your terminal that creates the virtual environment. 

The last item in the command is the name of the virtual environment folder. It will appear in your project folder after you run the command. 

You can name your virtual environment whatever your want, but the convention is to name it env or venv. In this example, we name it venv. 

After you run the command, look in your project folder. You should see a folder named venv.

For MacOS users, create a virtual environment by entering the following in your terminal:

```python
 python3 -m venv venv
```

For Windows users, create a virtual environment by entering the following in your terminal:

```python
py -m venv venv
```

Look inside your virtual environment. Among other things, you should see a folder named bin. It has a script you will use to activate your virtual environment. You also should see a folder named lib. It contains the software packages that you install in your project as dependencies.  

## [Activate Virtual Environment](#activate-virtual-environment)

Now that you created a virtual environment for your project, you need to activate it.  

Each time you open your project folder, you will need to activate your virtual environment.   

For MacOS users, inside your project folder, activate the virtual environment by entering the following in your terminal:  

```python
source venv/bin/activate
```

For Windows users, activate the virtual environment by entering the following in your terminal:  


```python
.\venv\Scripts\activate
```

Confirm you are in the virtual environment.  

In your terminal, if you see on the far left of the command line the name of your virtual environment inside parenthesis, then you have successfully activated your virtual environment.  

You can also confirm whether you are in your virtual environment using a terminal command.  

For macOS users, confirm that you are in your virtual environment by entering the following in your terminal:  

```python
which python
```

For Windows users, confirm that you are in your virtual environment by entering the following in your terminal: 

```python
where python
 ```

If your virtual environment is activated, your terminal will point you to the directory in which your virtual environment exists. For instance:  

```python
. . . /venv/bin/python
```

If your virtual environment is not activated, your terminal will point you to the directory in which your Python installation lives globally on your computer. For instance:  

```python
/usr/bin/python
```

To deactivate your virtual environment, type the following command in your terminal.  

```python
deactivate
```
For now, do not deactivate your virtual environment. You should continue working in it for the remainder of the tutorial.  

While still in your project folder, create a requirements.txt file. Instructions below. It will list the packages installed in your venv.  

Before you run the command below, look in your project folder and notice that it is missing a requirements.txt file.  

After running the command, look again. Your project folder should have a requirements.txt file.  

Run the below command in your terminal. It creates a requirements.txt file and lists all the installed dependencies.  

MacOS

```python
pip3 freeze > requirements.txt
```

Windows

```python
venv/bin/pip freeze > requirements.txt
```

If you look inside the requirements.txt file, it should be empty because you have not yet installed any dependencies. But you will do that soon.  

Meanwhile, also create a .gitignore file (starts with . and ends with no extension).  

Inside the .gitignore file, type venv and save the file. The .gitignore file lists the files that you do not want to save in the version tracking that we will use in later lessons. For now, just make it and get in the habit of using it.   

By having a requirements.txt file that lists the dependencies and a .gitignore file that lists the venv file containing the dependencies, you can save your code to GitHub without pushing all the dependency packages.  

Without including the dependencies, your code will download and upload more quickly and will take less storage space on GitHub. Then, when you or someone pulls the code from GitHub, you can install the dependencies listed in the requirements.txt file wit a single command.   

## [Install Flask](#install-flask)

Now that you created and activated your virtual environment, you can start installing packages.  

The first package you should install is Flask.

```python
pip3 install Flask
```

Next, in your terminal, again run the following command.


```python
pip3 freeze > requirements.txt 
```

This updates the requirements.txt file with the installed packages.  

After freezing your requirements.txt file, look at it. You should see an updated list of the packages installed for your project’s virtual environment. 

Yours should include Flask, any of the dependencies that Flask relies upon and automatically installs, plus any other packages you installed. 

Later, when you push your project folder to GitHub, notice that the venv folder is not pushed to GitHub, assuming you create a .gitignore file and list the venv folder in it.  

Sidenote: You can freeze as many times as you want. It is best to do so before deployment and also good practice to do so after installing one or more new packages.  


## [Create App File](#create-app-file)

In your project folder, create a file called app.py.

Copy the code below and paste it into your new file.

```python
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello World" 


if __name__ == "__main__":
    app.run(host="localhost", port=2000, debug=True, use_reloader=True)
```

In the [bare Flask app example](https://thacash.com/flask/code-samples/getting-started/bare-flask-app), you can learn what the code does and how it works.  

For now, all you need to know is that this file contains the code to run a simple server.  

## [Run App File](#run-app-file)

Now you can run the code. 

Start your server by typing in the terminal the following command:

```python
python3 app.py
```

You should see something like in the image below:

![flask-simple-server](https://app.thacash.com/wp-content/uploads/2022/02/flask-simple-server.png)

Your server is running!

It runs until you stop it or if it encounters a bug in your code.  

You can stop your server by pressing control + C.  

## [Next Lesson](#next-lesson)  

The [Bare Flask App](https://thacash.com/flask/code-samples/getting-started/bare-flask-app) code sample is the next step. 

