# 09_lambda.py

'''
Python Lambda Function

Lambda is a way to define a function. It is sometimes known as a lambda operator.
In differce to usual way to define function, lambda is anonymous, it does not need to be named.

It is used to create small one-line functions in purposes where normal function would be overkill.
'''

# Basic Example

# Classic function
def doubler(x):
    return x*2

print(doubler(5))
print(doubler(7))

# Lambda
doubler = lambda x: x*2

print(doubler(5))
print(doubler(8))

'''
Lambda is constructed as:

    lambda parametr: expression

Important characteristics:

    No Statements Allowed
        none of these: return, raise, pass, assert
    
    Single Expression only
        Unlike a normal function, a lambda function 
        contains only a single expression.

    Immediately Invoked Function Expression (IIFE)
        A lambda function can be immediately invoked.
        For this reason it is often referred to as 
        an Immediately Invoked Function Expression (IIFE). 

    Multiple Arguments
        You can send as many arguments as you like to a lambda 
        function; just separate them with comma.                    
'''


# Single Expression Only

even_odd = (lambda x: 
            'odd' if x%2 else 'even')       # 'odd' = 1 (True), else = 0 (False)

print(even_odd(3))
print(even_odd(4))

# Immediately Invoked Function Expression (IIFE)
print((lambda x: x*2)(3))

# Multiple Arguments

mul = lambda x, y: x*y
print(mul(77,82))


add = lambda x, y, z: x+y+z
print(add(77,87,88))

# -----------------------------------------------

'''
Ways to Pass Arguments

Like a normal function a lambda function supports all the different ways of passing
arguments. This includes
    Positional arguments
    Keyword arguments
    Default arguments
    Variable list of arguments(*args)
    Variable list of keyword arguments(**args)
'''

# Positional arguments (position of the arguments is decisive)
add = lambda x, y, z: x+y+z
print(add(2, 3, 4))

# Keyword arguments (arguments have a uniquely assigned value)
add = lambda x, y, z: x+y+z
print(add(2, y=3, z=4))

# Default arguments (arguments have default value that can be overriden)
add = lambda x, y=3, z=4: x+y+z
print(add(2))

# Variable list of arguments (arguments are available as a tuple)
add = lambda *args: sum(args)
print(add(2, 3, 4))

# Variable list of keyword  (arguments are available as a dict)
add = lambda **kwargs: sum(kwargs.values())
print(add(x=2, y=3, z=4))

'''
Lambdas with map(), filter() and reduce

    With map()
        The map() function expects two arguments: a function and a list. It takes that function
        and applies it on every item of the list and returns the modified list

    With filter()
        The filter() function is similar to the map(). It takes a function and applies it to each 
        item in the list to create a new list with only those items that cause the function 
        to return True.

    With reduce()
        reduce() is another Python function. It applies a rolling calculation to all items in a list.
        You can use it to calculate the total sum or to multiply all the numbers together.
'''

# map() function without lambda
def doubler(x):
    return x*2

L = [1, 2, 3, 4, 5, 6]

mod_list = map(doubler, L)
print(list(mod_list))

# with lambda, if you don't want to create a new function every time you use the map()
L = [1, 2, 3, 4, 5, 6]
doubler = map(lambda x: x*2, L)
print(list(doubler))

# filter() function without lambda
def check_age(age):
    if age > 18:
        return True
    else:
        return False

age = [5, 11, 16, 19, 24, 42]
adults = filter(check_age, age)
print(list(adults))

# with lambda
age = [5, 11, 16, 19, 24, 42]
adults = filter(lambda x: x > 18, age)
print(list(adults))

# reduce() without lambda

from functools import reduce

def summer(a, b):
    return a + b

L = [10, 20, 30, 40]
result = reduce(summer, L)
print(result)

# reduce() with lambda
from functools import reduce
L = [10, 20, 30, 40]
result = reduce(lambda x, y: x + y, L)
print(result)

'''
Return Multiple Values

    To return multiple values pack them in the tuple. Then use multiple assignment to unpack the parts
    of the returned tuple.
'''

# Return multiple values by packing them in the tuple
find_Square_Cube = lambda num: (num**2, num**3)
x, y = find_Square_Cube(2)
print(x)
print(y)

'''
if else in a Lambda
    Generally if else statement is used to implement selection logic in a function. But as it is a 
    statement, you cannot use it in a lambda function. You can use the if else ternary expression instead.
'''

# a lambda function that returns the smallest item
find_min = lambda x, y: x if y > x else y
print(find_min(2, 4))

'''
List Comprehension in a Lambda
    List comprehension is an expression, not a statement, so you can safely use it in a lambda function.
'''

# Flatten a nested list with lambda
flatten = lambda l: [item for sublist in l for item in sublist]

L = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(flatten(L))

l = [['a', 'b', 'C'], ['d', 'e']]
print(flatten(l))

'''
Jump Table Using a Lambda
    The jump table is a list or dictionary of functions to be called on demand. 
    Here’s how a lambda function is used to implement a jump table.
'''

# dictionary of functions
exponent = {
    'square': lambda x: x**2,
    'cube': lambda x: x**3
}

print(exponent['square'](3))
print(exponent['cube'](3))

# list of functions

exponent = [
    lambda x: x**2,
    lambda x: x**3
]

print(exponent[0](3))
print(exponent[1](3))

'''
Lambda Key Functions
    In Python, key functions are higher-order functions that take another function (which can be lambda function)
    as a key argument. This function directly changes the behavior of the key function itself.
    Here are some key functions:

    List method: sort()
    Built-in functions: sorted(), min(), max()
    In the Heap queue algorithm module heapq: nlargest() and smallest()
'''

# In the following example, a lambda is assigned to the key argument
# so that the list of students is sorted by their age rather than by name.

# Sort the list of tuples by the age of students

L = [
    ('Sam', 35),
    ('Max', 25),
    ('Bob', 30)
]

x = sorted(L, key=lambda student: student[1])
print(x)

'''
Lambda Closures
'''

# normal function

def multiplier(x):
    def inner_func(y):
        return x*y
    return inner_func

doubler = multiplier(2)
print(doubler(10))

tripler = multiplier(3)
print(tripler(10))

# Similary, a lambda can also be a closure. Here's the same example with a lambda function:

multiplier = (lambda x: (lambda y: x*y))
doubler = multiplier(2)
print(doubler(10))

tripler = multiplier(3)
print(tripler(10))