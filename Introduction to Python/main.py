import handcalcs.render

# First python output with 'Print' functions
print('Hello World!')
print('Hi, Python!')


# Python version check
import sys
print(sys.version) # version control
print(sys.winver) # [Windows only] version number of the Python DLL
print(sys.gettrace) # get the global debug tracing function
print(sys.argv) # keeps the parameters used while running the program we wrote in a list.


# The Python help function is used to display the documentation of modules, functions, classes, keywords, etc.
help(sys) # here the module name is 'sys'


# This is a comment, and to write a comment, '#' symbol is used.
print('Hello World!') # This line prints a string.
# Print 'Hello'
print('Hello')


# Print string as error message
frint('Hello, World!')

# Built-in error message
print('Hello, World!)

# Print both string and error to see the running order
print('This string is printed')
frint('This gives an error message')
print('This string will not be printed')


# String
print("Hello, World!")
# Integer
print(12)
# Float
print(3.14)
# Boolean
print(True)
print(False)
print(bool(1)) # Output = True
print(bool(0)) # Output = False


# String
print(type('Hello, World!'))
# Integer
print(type(15))
print(type(-24))
print(type(0))
print(type(1))
# Float
print(type(3.14))
print(type(0.5))
print(type(1.0))
print(type(-5.0))
# Boolean
print(type(True))
print(type(False))


# to obtain the information about 'interger' and 'float'
print(sys.int_info)
print() # to add a space between two outputs, use 'print()' function
print(sys.float_info)


# Let's convert the integer number 6 to a string and a float
number = 6
print(str(number))
print(float(number))
print(type(number))
print(type(str(number)))
print(type(float(number)))
str(number)



# Let's conver the float number 3.14 to a string and an integer
number = 3.14
print(str(number))
print(int(number))
print(type(number))
print(type(str(number)))
print(type(int(number)))
str(number)


# Let's convert the booleans to an integer, a float, and a string
bool_1 = True
bool_2 = False
print(int(bool_1))
print(int(bool_2))
print(float(bool_1))
print(float(bool_2))
print(str(bool_1))
print(str(bool_2))
print(bool(1))
print(bool(0))


# Let's find the data types of 9/3 and 9//4
print(9/3)
print(9//4)
print(type(9/3))
print(type(9//4))


# Addition
x = 56+65+89+45+78.5+98.2
print(x)
print(type(x))


# Substraction
x = 85-52-21-8
print(x)
print(type(x))


# Multiplication
x = 8*74
print(x)
print(type(x))


# Division
x = 125/24
print(x)
print(type(x))


# Floor division
x = 125//24
print(x)
print(type(x))


# Modulus
x = 125%24
print(x)
print(type(x))


# Exponentiation
x = 2**3
print(x)
print(type(x))



# An example: Let's calculate how many minutes there are in 20 hours?
one_hour = 60 # 60 minutes
hour = 20
minutes = one_hour *hour
print(minutes)
print(type(minutes))
# An example: Let's calculate how many hours there are in 348 minutes?
minutes = 348
one_hour = 60
hours = 348/60
print(hours)
print(type(hours))



# Mathematica expression
x = 45+3*89
y = (45+3)*89
print(x)
print(y)
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x**y)
print(x//y)
print(x%y)


# Store the value 89 into the variabe 'number'
number = 90
print(number)
print(type(number))


x = 25
y = 87
z = 5*x - 2*y
print(z)
t = z/7
print(t)
z = z/14
print(z)


x, y, z = 8, 4, 2 # the values of x, y, and z can be written in one line.
print(x, y, z)
print(x)
print(y)
print(z)
print(x/y)
print(x/z)
print(y/z)
print(x+y+z)
print(x*y*z)
print(x-y-z)
print(x/y/z)
print(x//y//z)
print(x%y%z)






