# PYTHON OPP
# MORE CLASSES AND OBJECTS

#Class
In Python, a class is a blueprint for creating objects (instances). It defines the attributes and methods that objects of the class will have

#Recap
In all the programs we wrote till now, we have designed our program around functions i.e. blocks of statements which manipulate data. This is called the procedure-oriented way of programming. There is another way of organizing your program which is to combine data and functionality and wrap it inside something called an object. This is called the object oriented programming paradigm. Most of the time you can use procedural programming, but when writing large programs or have a problem that is better suited to this method, you can use object oriented programming techniques.

Classes and objects are the two main aspects of object oriented programming. A class creates a new type where objects are instances of the class. An analogy is that you can have variables of type int which translates to saying that variables that store integers are variables which are instances (objects) of the int class.

# __doc__
__doc__ is a special attribute in Python that stores the documentation string (docstring) of a module, class, function, or method. A docstring is a string literal that occurs as the first statement in a module, function, class, or method definition, and it is used to document what the code does.

The __doc__ attribute allows you to access the docstring associated with a particular object. It can be accessed using dot notation or the getattr() function.

#__del__
__del__ is a special method in Python that serves as the destructor for a class. It is called when an object is about to be destroyed, i.e., when the object is no longer referenced by any part of the program and is eligible for garbage collection.

The __del__ method is the counterpart to the __init__ method, which is the constructor. While the __init__ method is called when an object is created, the __del__ method is called when the object is being destroyed.
