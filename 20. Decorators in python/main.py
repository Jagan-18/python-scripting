"""
@hello_decorator
def hi_decorator():
 print("Hello")
"""
'''
Above code is equal to -
def hi_decorator():
 print("Hello")

hi_decorator = hello_decorator(hi_decorator)
'''



# Import libraries
import decorator
from decorator import *
import functools
import math


help(decorator)




# Define a function
"""
In the following function, when the code was executed, it yeilds the outputs for both functions.
The function new_text() alluded to the function mytext() and behave as function.
"""
def mytext(text):
    print(text)
mytext('Python is a programming language.')
new_text = mytext
new_text('Hell, Python!')



def multiplication(num):
    return num * num
mult = multiplication
mult(3.14)


# Define a function
"""
In the following function, it is nonsignificant how the child functions are announced.
The implementation of the child function does influence on the output.
These child functions are topically linked with the function mytext(), therefore they can not be called individually.
"""
def mytext():
    print('Python is a programming language.')
    def new_text():
        print('Hello, Python!')
    def message():
        print('Hi, World!')

    new_text()
    message()
mytext()





# Define a function
"""
In the following example, the function text() is nesred into the function message().
It will return each time when the function tex() is called.
"""
def message():
    def text():
        print('Python is a programming language.')
    return text
new_message = message()






def function(num):
    def mult(num):
        return num*num

    output = mult(num)
    return output
mult(3.14)




def msg(text):
    'Hello, World!'
    def mail():
        'Hi, Python!'
    print(text)

    mail()
msg('Python is the most popular programming language.')



# Define a function
"""
In this function, the mult() and divide() functions as argument in operator() function are passed.
"""
def mult(x):
    return x * 3.14
def divide(x):
    return x/3.14
def operator(function, x):
    number = function(x)
    return number
print(operator(mult, 2.718))
print(operator(divide, 1.618))




def addition(num):
    return num + math.pi
def called_function(func):
    added_number = math.e
    return func(added_number)
called_function(addition)




def decorator_one(function):
    def inner():
        num = function()
    return num * (num**num)
    return inner
def decorator_two(function):
    def inner():
        num = function()
    return (num**num)/num
    return inner
@decorator_one
@decorator_two
def number():
    return 4
print(number())
# The above decorator returns the following code
x = pow(4, 4)/4
print(x*(x**x))



def msg_func():
    def text():
        return "Python is a programming language."
    return text
msg = msg_func()
print(msg())



# Define a decorating function
"""
In the following example, the function outer_addition that is some voluminous is decorated.
"""
def addition(a, b):
    print(a+b)
def outer_addition(func):
    def inner(a, b):
        if a < b:
            a, b = b, a
    return func(a, b)
    return inner
result = outer_addition(addition)
result(math.pi, math.e)






"""
Rather than above function, Python ensures to employ decorator in easy way with the symbol @ called 'pie' syntax, as
"""
def outer_addition(function):
    def inner(a, b):
        if a < b:
            a, b = b, a
    return function(a, b)
    return inner
@outer_addition # Syntax of decorator
def addition(a, b):
    print(a+b)
result = outer_addition(addition)
result(math.pi, math.e)




def decorator_text_uppercase(func):
    def wrapper():
        function = func()
    text_uppercase = function.upper()
    return text_uppercase
    return wrapper
# Using a function
def text():
    return 'Python is the most popular programming language.'
decorated_result = decorator_text_uppercase(text)
print(decorated_result())
# Using a decorator
@decorator_text_uppercase
def text():
    return 'Python is the most popular programming language.'
print(text())




def do_twice(function):
    def wrapper_do_twice():
        function()
    function()
    return wrapper_do_twice
@do_twice
def text():
    print('Python is a programming language.')
text()



def do_twice(function):
    """
    The function wrapper_function() can admit any number of argument and pass them on the function.
    """
    def wrapper_function(*args, **kwargs):
        function(*args, **kwargs)
    function(*args, **kwargs)
    return wrapper_function
@do_twice
def text(programming_language):
    print(f'{programming_language} is a programming language.')
text('Python')




@do_twice
def returning(programming_language):
    print('Python is a programming language.')
    return f'Hello, {programming_language}'
hello_python = returning('Python')





class Microorganism:
    def __init__(self, name, product):
        self.name = name
    self.product = product
    @property
    def show(self):
        return self.name + ' produces ' + self.product + ' enzyme'
organism = Microorganism('Aspergillus niger', 'inulinase')
print(f'Microorganism name: {organism.name}')
print(f'Microorganism product: {organism.product}')
print(f'Message: {organism.show}.')




class Micoorganism:
    @staticmethod
    def name():
        print('Aspergillus niger is a fungus that produces inulinase enzyme.')
organims = Micoorganism()
organims.name()
Micoorganism.name()



class Microorganism:
    def __init__(self, name, product):
        self.name = name
    self.product = product

    @classmethod
    def display(cls):
        return cls('Aspergillus niger', 'inulinase')
organism = Microorganism.display()
print(f'The fungus {organism.name} produces {organism.product} enzyme.')




"""
In the following example, @iterate refers to a function object that can be called in another function.
The @iterate(numbers=4) will return a function which behaves as a decorator.
"""
def iterate(numbers):
    def decorator_iterate(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            for _ in range(numbers):
                worth = function(*args, **kwargs)
                return worth
            return wrapper
    return decorator_iterate
@iterate(numbers=4)
def function_one(name):
    print(f'{name}')
x = function_one('Python')




def arguments(func):
    def wrapper_arguments(argument_1, argument_2):
        print(f'The arguments are {argument_1} and {argument_2}.')
    func(argument_1, argument_2)
    return wrapper_arguments
@arguments
def programing_language(lang_1, lang_2):
    print(f'My favorite programming languages are {lang_1} and {lang_2}.')
programing_language("Python", "R")




def splitted_text(text):
    def wrapper():
        function = text()
    text_splitting = function.split()
    return text_splitting
    return wrapper
@splitted_text
@decorator_text_uppercase # Calling other decorator above
def text():
    return 'Python is the most popular programming language.'
text()




def arbitrary_argument(func):
    def wrapper(*args,**kwargs):
        print(f'These are positional arguments {args}.')
    print(f'These are keyword arguments {kwargs}.')
    func(*args)
    return wrapper
"""1. Without arguments decorator"""
print(__doc__)
@arbitrary_argument
def without_argument():
    print("There is no argument in this decorator.")
without_argument()
"""2. With positional arguments decorator"""
print(__doc__)
@arbitrary_argument
def with_positional_argument(x1, x2, x3, x4, x5, x6):
    print(x1, x2, x3, x4, x5, x6)
with_positional_argument(math.inf, math.tau, math.pi, math.e, math.nan, -math.inf)
"""3. With keyword arguments decorator"""
print(__doc__)
@arbitrary_argument
def with_keyword_argument():
    print("Python and R are my favorite programming languages and keyword arguments.")
with_keyword_argument(language_1="Python", language_2="R")




def capitalize_dec(function):
    @functools.wraps(function)
    def wrapper():
        return function().capitalize()
    return wrapper
@capitalize_dec
def message():
    "Python is the most popular programming language."
    return 'PYTHON IS THE MOST POPULAR PROGRAMMING LANGUAGE. '
print(message())
print()
print(message.__name__)
print(message.__doc__)


def preserved_decorator(function):
    def wrapper():
        print('Before calling the function, this is printed.')
    function()
    print('After calling the function, this is printed.')
    return wrapper
@preserved_decorator
def message():
    """This function prints the message when it is called."""
    print('Python is the most popular programming language.')
message()
print(message.__name__)
print(message.__doc__)
print(message.__class__)
print(message.__module__)
print(message.__code__)
print(message.__closure__)
print(message.__annotations__)
print(message.__dir__)
print(message.__format__)

