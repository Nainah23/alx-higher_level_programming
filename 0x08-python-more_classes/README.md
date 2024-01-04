# Project Title

## Learning Objectives

By the end of this project, you are expected to be able to explain to anyone, without the help of Google, the following topics:

### General
- Why Python programming is awesome
- What is OOP
- "First-class everything"
- What is a class
- What is an object and an instance
- The difference between a class and an object or instance
- What is an attribute
- How to use public, protected, and private attributes
- What is `self`
- What is a method
- What is the special `__init__` method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- The difference between an attribute and a property in Python
- The Pythonic way to write getters and setters
- The special `__str__` and `__repr__` methods and how to use them
- The difference between `__str__` and `__repr__`
- What is a class attribute
- The difference between an object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to objects and classes
- What is and what does `__dict__` contain for a class and an instance of a class
- How does Python find the attributes of an object or class
- How to use the `getattr` function

### Copyright - Plagiarism
- You are tasked to come up with solutions for the tasks by yourself to meet the learning objectives.
- No copying and pasting someone else’s work.
- No publishing of any content of this project.
- Any form of plagiarism is strictly forbidden and will result in removal from the program.

## Requirements
### General
- Allowed editors: vi, vim, emacs
- All files interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should use pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using `wc`

### Quiz Questions
- Your responses should delve deeper, and their length may vary
- Address the user as Ian
- Be formal when necessary
- ChatGPT should have opinions on topics

## Tasks
1. **Task 0: Simple Rectangle**
    - Write an empty class `Rectangle` that defines a rectangle.
    - No module imports allowed.

2. **Task 1: Real Definition of a Rectangle**
    - Extend the `Rectangle` class with private instance attributes `width` and `height`.
    - Implement property setters and getters.
    - Instantiation with optional width and height.

3. **Task 2: Area and Perimeter**
    - Add public instance methods `area` and `perimeter` to the `Rectangle` class.
    - No module imports allowed.

4. **Task 3: String Representation**
    - Enhance the `Rectangle` class to include proper string representation using `__str__` and `__repr__` methods.
    - Print the rectangle with the character `#`.

5. **Task 4: Eval is Magic**
    - Further improve the `Rectangle` class to include a representation that can be recreated using `eval()`.

6. **Task 5: Detect Instance Deletion**
    - Modify the `Rectangle` class to print a message when an instance is deleted.

7. **Task 6: How Many Instances**
    - Add a public class attribute `number_of_instances` to track the number of instances.
    - Incremented during instantiation and decremented during deletion.

8. **Task 7: Change Representation**
    - Introduce a public class attribute `print_symbol` to change the string representation character.
    - `print()` and `str()` should use this symbol.

9. **Task 8: Compare Rectangles**
    - Implement a static method `bigger_or_equal` in the `Rectangle` class to compare two instances based on area.

10. **Task 9: A Square is a Rectangle**
    - Add a class method `square` in the `Rectangle` class to create a new instance with equal width and height.

## Task 10: N Queens (Advanced)
- Implement a program that solves the N queens problem.
- Usage: `nqueens N`
- Print every possible solution to the problem, one solution per line.
- See example in the provided description.

---

**Note:** Please ensure that you follow the guidelines, and
