Tasks Project
Introduction
This project involves creating classes in Python for geometric shapes like Rectangle and Square. Each class is tested, validated, and comes with various methods for manipulation.

Installation
No specific installation is required. Simply include the relevant files in your project.

Usage
Base class:

Create a folder named models with an empty file __init__.py inside.
Implement a class Base with an id attribute management system.
python
Copy code
from models.base import Base

b1 = Base()
print(b1.id)
First Rectangle:

Implement a class Rectangle that inherits from Base.
Validate attributes like width, height, x, and y.
python
Copy code
from models.rectangle import Rectangle

r1 = Rectangle(10, 2)
print(r1.id)
Validate attributes:

Update the Rectangle class to include attribute validation.
python
Copy code
r = Rectangle(10, "2")  # Raises TypeError
Area first:

Add a method area to calculate the area of a Rectangle instance.
python
Copy code
r1 = Rectangle(3, 2)
print(r1.area())
Display #0:

Implement a method display to print the Rectangle instance using '#'.
python
Copy code
r1 = Rectangle(4, 6)
r1.display()
str:

Override the __str__ method in Rectangle to customize its string representation.
python
Copy code
r1 = Rectangle(4, 6, 2, 1, 12)
print(r1)
Display #1:

Improve the display method to consider x and y coordinates.
python
Copy code
r1 = Rectangle(2, 3, 2, 2)
r1.display()
Update #0:

Add an update method to Rectangle that assigns values based on arguments.
python
Copy code
r1 = Rectangle(10, 10, 10, 10)
r1.update(89, 2, 3, 4, 5)
print(r1)
Update #1:

Enhance the update method to accept key-value pairs.
python
Copy code
r1 = Rectangle(10, 10, 10, 10)
r1.update(width=1, x=2)
print(r1)
And now, the Square!:

Create a class Square that inherits from Rectangle.
Implement its constructor and ensure width and height are the same.
python
Copy code
from models.square import Square

s1 = Square(5)
print(s1)
Square size:
Add getter and setter methods for the size attribute in the Square class.
python
Copy code
s1 = Square(5)
print(s1.size)
Square update:
Implement an update method for the Square class similar to the Rectangle class.
python
Copy code
s1 = Square(5)
s1.update(1, 2, 3, 4)
print(s1)
Rectangle instance to dictionary representation:
Add a method to_dictionary to convert a Rectangle instance to a dictionary.
python
Copy code
r1 = Rectangle(10, 2, 1, 9)
r1_dictionary = r1.to_dictionary()
print(r1_dictionary)
Square instance to dictionary representation:
Implement a to_dictionary method for the Square class.
python
Copy code
s1 = Square(10, 2, 1)
s1_dictionary = s1.to_dictionary()
print(s1_dictionary)
Dictionary to JSON string:
Add a static method to_json_string in the Base class to convert a list of dictionaries to a JSON string.
python
Copy code
r1 = Rectangle(10, 2, 1, 9)
dictionary_list = [r1.to_dictionary()]
json_string = Base.to_json_string(dictionary_list)
JSON string to file:
Update the Base class with a class method save_to_file to save a JSON string to a file.
python
Copy code
r1 = Rectangle(10, 2, 1, 9)
r2 = Rectangle(2, 4)
Rectangle.save_to_file([r1, r2])
JSON string to dictionary:
Add a static method from_json_string in the Base class to convert a JSON string to a list of dictionaries.
python
Copy code
json_string = '[{"width": 10, "height": 4}, {"width": 1, "height": 7}]'
dictionary_list = Base.from_json_string(json_string)
Dictionary to Instance:
Implement a class method create in the Base class to create an instance from a dictionary.
python
Copy code
r1 = Rectangle(3, 5, 1)
r1_dictionary = r1.to_dictionary()
r2 = Rectangle.create(**r1_dictionary)
File to instances:
Update the Base class with a class method load_from_file to load instances from a file.
python
Copy code
list_rectangles_input = Rectangle.load_from_file()
