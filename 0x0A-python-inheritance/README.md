Learning Objectives
General:

Understand the awesomeness of Python programming
Comprehend superclass, base class, and subclass concepts
List attributes and methods of a class or instance
Identify when an instance can have new attributes
Inherit a class from another and define classes with multiple base classes
Recognize the default class every class inherits from
Override inherited methods or attributes
Understand the purpose of inheritance
Utilize isinstance, issubclass, type, and super built-in functions
Copyright - Plagiarism:

Develop solutions independently to meet learning objectives
Strictly avoid plagiarism and refrain from publishing project content
Requirements:

Write Python scripts using allowed editors (vi, vim, emacs)
Use Python 3.8.5 on Ubuntu 20.04 LTS
Follow specific file and code structure guidelines
Use pycodestyle for code formatting
Create a mandatory README.md file
Ensure all files are executable
Python Test Cases:

Write test cases in text files inside a 'tests' folder
Execute tests using the command 'python3 -m doctest ./tests/*'
Include proper documentation for modules, classes, and functions
Encourage collaboration on test cases to cover various scenarios
Documentation:

Avoid using 'import' or 'from' inside comments
Quiz Questions:

Successfully complete the quiz to proceed
Tasks
0. Lookup
Write a function to return a list of attributes and methods of an object.

python
Copy code
def lookup(obj):
    """Returns a list object"""
1. My list
Create a class MyList that inherits from list and prints a sorted list.

python
Copy code
class MyList(list):
    """MyList class that inherits from list"""
    def print_sorted(self):
        """Prints the list, sorted (ascending sort)"""
2. Exact same object
Write a function to check if an object is an exact instance of a specified class.

python
Copy code
def is_same_class(obj, a_class):
    """Returns True if obj is exactly an instance of a_class; otherwise False"""
3. Same class or inherit from
Function to check if an object is an instance of a class or inherited from it.

python
Copy code
def is_kind_of_class(obj, a_class):
    """Returns True if obj is an instance of or inherited from a_class; otherwise False"""
4. Only sub class of
Function to check if an object is an instance of a class inherited (directly or indirectly).

python
Copy code
def inherits_from(obj, a_class):
    """Returns True if obj is an instance of a class inherited (directly or indirectly) from a_class; otherwise False"""
5. Geometry module
Create an empty class BaseGeometry.

python
Copy code
class BaseGeometry:
    """Empty class BaseGeometry"""
6. Improve Geometry
Extend BaseGeometry with a method raising an Exception.

python
Copy code
class BaseGeometry:
    """BaseGeometry class with a method that raises an Exception"""
    def area(self):
        """Raises an Exception with the message 'area() is not implemented'"""
7. Integer validator
Extend BaseGeometry with a method to validate integers.

python
Copy code
class BaseGeometry:
    """BaseGeometry class with a method for integer validation"""
    def integer_validator(self, name, value):
        """Validates an integer value"""
8. Rectangle
Create a class Rectangle inheriting from BaseGeometry.

python
Copy code
class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes Rectangle with width and height"""
9. Full rectangle
Extend Rectangle to implement area and format description.

python
Copy code
class Rectangle(BaseGeometry):
    """Rectangle class inheriting from BaseGeometry with area and description"""
    def __init__(self, width, height):
        """Initializes Rectangle with width and height"""
    def __str__(self):
        """Returns formatted rectangle description [Rectangle] <width>/<height>"""
10. Square #1
Create a class Square inheriting from Rectangle.

python
Copy code
class Square(Rectangle):
    """Square class inheriting from Rectangle"""
    def __init__(self, size):
        """Initializes Square with size"""
11. Square #2
Extend Square to implement area and format description.

python
Copy code
class Square(Rectangle):
    """Square class inheriting from Rectangle with area and description"""
    def __init__(self, size):
        """Initializes Square with size"""
    def __str__(self):
        """Returns formatted square description [Square] <size>
