
Project README.md
Overview
This repository, alx-higher_level_programming, contains a series of JavaScript files organized under the directory 0x13-javascript_objects_scopes_closures. Each JavaScript file corresponds to a task related to defining classes, inheritance, and implementing various methods. The tasks involve creating and manipulating objects, demonstrating object-oriented programming principles in JavaScript.

Project Structure
0-rectangle.js
Defines an empty class Rectangle using the class notation.
1-rectangle.js
Defines a class Rectangle with a constructor that takes width (w) and height (h) as arguments.
Initializes the instance attributes width and height with the provided values.
2-rectangle.js
Similar to task 1 but includes a check: if w or h is equal to 0 or not a positive integer, an empty object is created.
3-rectangle.js
Extends the previous tasks by adding an instance method print() that prints the rectangle using the character 'X'.
4-rectangle.js
Adds two additional instance methods: rotate() exchanges the width and height, and double() multiplies both width and height by 2.
5-square.js
Defines a class Square that inherits from Rectangle and extends it.
Constructor takes a single argument size, and it calls the parent class's constructor using super().
6-square.js
Extends the Square class from task 5 and includes an instance method charPrint(c) that prints the square using the character c. If c is undefined, it defaults to 'X'.
7-occurrences.js
Exports a function nbOccurences(list, searchElement) that returns the number of occurrences of searchElement in the given list.
8-esrever.js
Exports a function esrever(list) that returns the reversed version of a list without using the built-in reverse method.
9-logme.js
Exports a function logMe(item) that prints the number of arguments already printed and the new argument value.
10-converter.js
Exports a function converter(base) that converts a number from base 10 to another base passed as an argument.
100-map.js
Imports an array from 100-data.js and computes a new array using the map function.
101-sorted.js
Imports a dictionary of occurrences by user id from 101-data.js and computes a new dictionary of user ids by occurrence.
102-concat.js
Concatenates two files. The first argument is the file path of the first source file, the second argument is the file path of the second source file, and the third argument is the file path of the destination.
