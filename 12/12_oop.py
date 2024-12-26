# https://www.freecodecamp.org/news/how-to-use-oop-in-python/

'''
Object Oriented Programming in Python
    Damilola Oladele
'''

# heavily relies on objects
# these objects can have attributes and methods
# while attributes store data, methods define behavior

# OOP becomes valuable when writing large-sized and complex program

'''
Why Use Object-Oriented Programming?
'''

# by grouping related data and functions into logical classes, OOP promotes code structure and simplifies maintananance
# the modular approach makes it easier to understand, modify, and reuse code, thereby reducing development time
# ability to provide a clear and relatable programming style
# the use of objects and the relationships between them mirror real-world concepts

"""
How to Define a Class in Python
"""

class Speaker:
    brand = "Beatpill" # class attribute

    def __init__(self, color, model):
        self.color = color # instance attribute
        self.model = model # instance attribute
    
    def power_on(self):
        print(f'Powering on {self.color} {self.model} speaker.')

    def power_off(self):
        print(f'Powering off {self.color} {self.model} speaker.')

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color


speaker_one = Speaker('black', '85XB5')
speaker_two = Speaker('red', 'Y8F33')



#  <__main__.Speaker object at 0x0000019CF6156210>
# 0x0000019CF6156210 is a memory adress where Python stores the object


if speaker_one == speaker_two:
    print('speaker one is the same as speaker two')
else:
    print('speaker one is different from speaker two')

'''
Class and Instance Attributes
'''

# while class attributes are common to all instances created from my class, instance attributes are unique to each instance
# class attributes are variables that belong to the class itself, rather than to individual instances of the class
# the effect of class attributes is that all instances you create from your class will inherit and share that class
# attribute and its value. In this case, every instance you create from your Speaker class will share the same brand value


print(f'Speaker one is {speaker_one.color} while speaker two is {speaker_two.color}.',
speaker_one.brand,
speaker_two.brand,
sep='\n',
)

'''
Instance Methods

    In addition to class and instance attributes, classes can also have methods, known as instance
    methods. Instance methods are functions defined within a class that operate on instances of the class.
    They use the class and instance attributes to provide behavior and functionality to objects.

'''

speaker_one.power_on()
speaker_two.power_off()


'''
Encapsulation in Python

    Encapsulation is one of the core concepts of OOP. It refers to the bundling
    of data (attributes) and methods within a class. Encapsulation provides data
    protection and control over how the code interacts with an object's internal
    state.

    You can achieve encapsulation in Python by defininig private attributes and
    methods within a class. By convention, private attributes and methods are 
    prefixed with a single underscore(_). While Python does not have strict
    private modifiers like some other languages, the underscore prefix serves
    as a warning to other developers not to access or modify the attributes and 
    methods directly from outside the class.

    Encapsulation promotes code modularity, maintainability, and data
    protection by separating the internal state from the public interface
    (methods). It allows you to change the internal state without affecting the
    code that uses the class, as long as the public interface remains the same.
'''

class Speaker:
    brand = "Beatpill"

    def __init__(self, color, model):
        self._color = color  # Private attribute
        self._model = model  # Private attribute

    def power_on(self):
        print(f"Powering on {self._color} {self._model} speaker.")

    def power_off(self):
        print(f"Powering off {self._color} {self._model} speaker.")

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        self._color = new_color


speaker_one = Speaker("black", "85XB5")
speaker_one.power_on()

# Accessing a private attribute directly (not recommended)
print(speaker_one._color)

# Accessing a private attribute using the getter method (recommended)
print(speaker_one.get_color())

# Modifying a private attribute using the setter method (recommended)
speaker_one.set_color("white")
print(speaker_one.get_color())

'''
Inheritance in Python

    Inheritance is another core concept of OOP. I allows classes to inherit
    attributes and methods from other classes. The new class inherits
    attributes and methods from the existing class, known as the parent or base
    class. The new class is called the child or derived class.

    Inheritence promotes code reuse by allowing the child class to inherit and
    extend the functionality of the parent class. This helps in creating
    hierarchichal relationships between classes and organizing code in a more
    structured and logical manner.

'''

# In Python, inheritance is implemented using the following syntax:

class DerivedClass(Speaker):
    # Derived class methods and attributes
    pass

# Add a SmartSpeaker class and make it inherit from the Speaker class

class SmartSpeaker(Speaker):
    def __init__(self, color, model, voice_assistant):
        super().__init__(color, model)
        self._voice_assistant = voice_assistant

    def say_hello(self):
        print(f"Hello, I am {self._voice_assistant}")

# Create an instance of the SmartSpeaker class
smart_speaker = SmartSpeaker('black', 'XYZ123', 'Alexa')
smart_speaker.power_on() # inherited from Speaker class
smart_speaker.say_hello()

'''
The __init__ method of the SmartSpeaker class calls the __init__
method of the Speaker class using super().__init__(color, model). This
ensures that the inherited _color and _model attributes are properly
initialized. Also, the SmartSpeaker class has its own attribute
_voice_assistant, and a new method say_hello.
'''

# --------------------------------------------------------------------------------------------------------

# https://www.learnbyexample.org/python-classes-and-objects/

'''
Python Classes and Objects

    To create your own custom objects in Python, you first need to define a class, using the
    keyword class.

    Suppose you want to create objects to represent information about cars. Each object will
    represent a single car. You'll first need to define a class called Car.
'''

# Here's the simpliest possible class (empty one):

class Car:
    pass

'''
The __init__() Method

    __init__() is the special method that initializes an individual object. This method runs
    automatically each time an object of a class is created.

    The __init__() method is generally used to perform operations that are necessary before
    the object is created.
'''

class Car:
    
    # initializer
    def __init__(self):
        pass


# when you define __init__() in a class definition, its first parameter should be self.

'''
The Self Parameter

    The self parameter refers to the individual object itself. It is used to fetch or se attributes
    of the particular instance.

    This parameter doesn't have to be called self, you can call it whatever you want, but it is
    standard practice, and you should probably stick with it.

    !! self should be the first parameter of any method in the class, even if the
    method does not use it.
'''

'''
Attributes

    Every class you write in Python has two basic features: attributes and methods.

    Attributes are the individual things that differentiate one object from another. They
    determine the appearance, state, or other qualities of the object.

    In our case, the 'Car' class might have the following attributes:

    Style: Sedan, SUV, Coupe
    Color: Silver, Black, White
    Wheels: Four

    Attributes are defined in classes by variables, and each object can have its own values for
    those variables.

    There are two types of attributes: Instance attributes and Class attributes.
'''

'''
Instance Attribute

    The instance attribute is a variable that is unique to each object (instance). Every object of
    that class has its own copy of that variable. Any changes made to the variable don't reflect
    in other objects of that class.
'''

# In the case of our Car() class, each car has a specific color and style.

class Car:

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style


'''
Class Attribute

    The class attribute is a variable that is for all objects. And there's only once copy of that
    variable that is shared with all objects. Any changes made to that variable will reflect in all
    other objects.
'''

# In the case of our Car() class, each car has 4 wheels.

class Car:

    # class attribute
    wheels = 4

    # initializer with instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

'''
Create an Object

    You create an object of a class by calling the class name and passing arguments as if it were
    a function.
'''

c = Car('Sedan', 'Black')

'''
    Here we created a new object from the Car class by passing strings for the style and color
    parameters. But, we did't pass in the self argument.

    This is because, when you create a new object, Python automatically determines what self is
    (our newly-created object in this case) and passes it to the __init__ method.
'''

'''
Access and Modify Attributes

    The attributes of an instance are accessed and assigned to by using dot '.' notation.
'''

# Access attributes
print(c.style) # prints -> Sedan
print(c.color) # prints -> Black

# Modify attribute
c.style = 'SUV'
print(c.style) # prints -> SUV

'''
Methods

    Methods determine what type of functionality a class has, how it handles its data, and its
    overall behavior. Without methods, a class would simply be a structure.

    In our case, the 'Car' class might have the following methods:

    > Change color

    > Start engine

    > Stop engine

    > Change gear

    Just as there are instance and class attributes, there are also instance and class methods.
    Instance methods operate on an instance of a class; whereas class methods operate on the
    class itself
'''

'''
Instance Methods

    Instance methods are nothing but functions defined inside a class that operates on 
    instances of that class.
'''
# Now let's add some methods to the class
# show_description() method: to print the current values of all the instance attributes
# change_color() method: to change the value of 'color' attribute

class Car:

    # class attribute
    wheels = 4

    # initializer / instance attributes
    def __init__(self, color, style):
        self.color = color
        self.style = style

    # method 1
    def show_description(self):
        print(f'This car is a {self.color} {self.style}')

    # method 2
    def change_color(self, new_color):
        self.color = new_color


c = Car('Blue', 'Van')

c.show_description()
c.change_color('Pink')
c.show_description()
    
'''
Delete Attributes and Objects

    to delete any object attribute, use the del keyword.
'''

del c.color

# You can delete the object completely with del keyword.

del c
