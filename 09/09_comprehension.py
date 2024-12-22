# 09_comprehension.py

''' 
List comprehension

The general syntax for a list of comprehension is:

        [expression for var in iterable]
'''

# 0
sqrt_list = [x**2 for x in range(101)]
print(sqrt_list)

# 1
# List of comprehension can iterate over any kind of iterable such as lists, strings, files, ranges

L = [x * 3 for x in 'RED']
print(L)

# 2
# abs() function converts to absolute values

vec = [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
l = [abs(x) for x in vec]
print(l)

# 3

colors = [' red', ' green ', 'blue ', '     black   ', '                pink                    ']
l = [x.strip() for x in colors]
print(l)


# 4
# if list of comprehension creates a tuples, these must be in parentheses

l = [(x, x*2) for x in range(9)]
print(l)

# more complex but kind of the same:

l = [((x, x*2), (x, x**2)) for x in range(3)]
print(l)


'''
List comprehension with if clause

Iterable's items are skipped for which the if clause is not true
The general syntax for a list of comprehension is:

        [expression for var in iterable if_clause]

'''

# 0
# filter list to exclude negative numbers

num = [-5, 4, -1, 2, 2, 3, -1, 4, 5, -1]
l = [x for x in num if x > 0]
print(l)

'''
Nested List Comprehensions
The initial expression in a list comprehension can be any expression,
including another list comprehension.

        [expression for variable in iterable for variable in iterable]
'''

# 0
vector = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
l = [number for list in vector for number in list]
print(l)

goals = ['Specific', 'Measurable', 'Achievable', 'Realistic', 'Time-Bound']
l = [letter for string in goals for letter in string if letter in 'TMSAR']
print(l)


matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

l = [[row[i] for row in matrix] for i in range(3)]
print(l)

matrix = [['x', 'o', 'x'],
          ['o', 'x', 'o'],
          ['x', 'o', 'x']]

l = [i for row in matrix for i in row]
print(l)

# 1

'''
List Comprehension vs map() + lambda

If calling an existing function on each element, map(f, L) is a bit faster than the corresponding
list comprehension [f(x) for x in L].

Following example collects the ASCII codes of all characters in an entire string.
'''

# With list comprehension
L = [ord(x) for x in 'foo']
print(L)

L = list(map(ord, 'foo'))
print(L)

'''
However, when evaluating any other expression, [some_expr for x in L] is faster and clearer than map(lambda x: some_expr, L), 
because the map incurs an extra function call for each element. Following example creates a list of all integer square numbers.
'''

# With list comprehension

L = [x**2 for x in range(5)]
print(L)

# With map() function

L = list(map((lambda x: x**2), range(5)))
print(L)


'''
List comprehension vs filter() + lambda

List comprehension with if clause can be thought of as analogous to the filter() function as they both skip an iterable’s items
for which the if clause is not true. Following example filters a list to exclude odd numbers.
'''

# With list comprehension

L = [x for x in range(10) if x % 2 == 0]
print(L)


# With filter() function

L = list(filter((lambda x: x % 2 == 0), range(10)))
print(L)