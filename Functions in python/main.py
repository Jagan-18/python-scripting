# Take a function sample
# Mathematical operations in a function
def process(x):
    y1 = x-8
    y2 = x+8
    y3 = x*8
    y4 = x/8
    y5 = x%8
    y6 = x//8
    print(f'If you make the above operations with {x}, the results will be {y1}, {y2}, {y3}, {y4}, {y5}, {y6}.')
    return y1, y2, y3, y4, y5, y6
process(5)


help(process)


process(3.14)


# Define a function with multiple elements
def mult(x, y):
    z = 2*x + 5*y + 45
    return z
output = mult(3.14, 1.618) # You can yield the output by assigning to a variable
print(output)
print(mult(3.14, 1.618)) # You can obtain the result directly
mult(3.14, 1.618) # This is also another version



# Call again the defined function with different arguments
print(mult(25, 34))


# Define a function
def function(x):

    # Take a local variable
    y = 3.14
    z = 3*x + 1.618*y
    print(f'If you make the above operations with {x}, the results will be {z}.')
    return z
with_golden_ratio = function(1.618)
print(with_golden_ratio)



# It starts the gloabal variable
a = 3.14
# call function and return function
y = function(a)
print(y)



# Enter a number directly as a parameter
function(2.718)


# Define a function with and without return statement
def msg1():
    print('Hello, Python!')
def msg2():
    print('Hello, World!')
    return None
msg1()
msg2()



# Printing the function after a call indicates a None is the default return statement.
# See the following prontings what functions returns are.
print(msg1())
print(msg2())



# Define a function
def strings(x, y):
    return x + y
# Testing the function 'strings(x, y)'
strings('Hello', ' ' 'Python')


# The following codes are not used again.
x = 2.718
y = 0.577
equation = x*y + x+y - 37
if equation>0:
    equation = 6
else: equation = 37
equation



# The following codes are not used again.
x = 0
y = 0
equation = x*y + x+y - 37
if equation<0:
    equation = 0
else: equation = 37
equation


# The following codes can be write as a function.
def function(x, y):
    equation = x*y + x+y - 37
    if equation>0:
        equation = 6
    else: equation = 37
    return equation
x = 2.718
y = 0.577
function(x, y)



# The following codes can be write as a function.
def function(x, y):
    equation = x*y + x+y - 37
    if equation<0:
        equation = 6
    else: equation = 37
    return equation
x = 0
y = 0
function(x, y)



# print() is a built-in function
special_numbers = [0.577, 2.718, 3.14, 1.618, 1729, 6, 28, 37]
print(special_numbers)


# The function sum() add all elements in a list or a tuple
sum(special_numbers)



# The function len() gives us the length of the list or tuple
len(special_numbers)



# Define a function including conditions if/else
def fermentation(microorganism, substrate, product, activity):
    print(microorganism, substrate, product, activity)
    if activity < 1000:
        return f'The fermentation process was unsuccessful with the {product} activity of {activity} U/mL from {substrate}
    else:
    return f'The fermentation process was successful with the {product} activity of {activity} U/mL from {substrate} us
result1 = fermentation('Aspergillus niger', 'molasses', 'inulinase', 1800)
print(result1)
print()
result2 = fermentation('Aspergillus niger', 'molasses', 'inulinase', 785)
print(result2)


# Define a function using the loop 'for'
def fermentation(content):
    for parameters in content:
        print(parameters)
content = ['Stirred-tank bioreactor' ,'30°C temperature', '200 rpm agitation speed', '1 vvm aeration', '1% (v/v) inoculum
           fermentation(content)


# Define a function adjusting the default value of the variable
def rating_value(rating = 5.5):
    if rating < 8:
        return f'You should not watch this film with the rating value of {rating}'
    else:
    return f'You should watch this film with the rating value of {rating}'
print(rating_value())
print(rating_value(8.6))


# Define a function for a global variable
language = 'Python'
def lang(language):
    global_var = language
    print(f'{language} is a program language.')
lang(language)
lang(global_var)
"""
The output gives a NameError, since all variables in the function are local variables,
so variable assignment is not persistent outside the function.
"""



# Define a function for a global variable
language = 'JavaScript'
def lang(language):
    global global_var
    global_var = 'Python'
    print(f'{language} is a programing language.')
lang(language)
lang(global_var)



process = 'Continuous fermentation'
def fermentation(process_name):
    if process_name == process:
        return '0.5 g/L/h.'
    else:
    return '0.25 g/L/h.'
print('The productiovity in continuous fermentation is', fermentation('Continuous fermentation'))
print('The productiovity in batch fermentation is', fermentation('Batch fermentation'))
print('Continuous fermentation has many advantages over batch fermentation.')
print(f'My favourite process is {process}.')



# If the variable 'process' is deleted, it returns a NameError as follows
del process
# Since the variable 'process' is deleted, the following function is an example of local variable
def fermentation(process_name):
    process = 'Continuous fermentation'
    if process_name == process:
        return '0.5 g/L/h.'
    else:
    return '0.25 g/L/h.'
print('The productiovity in continuous fermentation is', fermentation('Continuous fermentation'))
print('The productiovity in batch fermentation is', fermentation('Batch fermentation'))
print('Continuous fermentation has many advantages over batch fermentation.')
print(f'My favourite process is {process}.')



# When the global variable and local variable have the same name:
process = 'Continuous fermentation'
def fermentation(process_name):
    process = 'Batch fermentation'
    if process_name == process:
        return '0.5 g/L/h.'
    else:
    return '0.25 g/L/h.'
print('The productiovity in continuous fermentation is', fermentation('Continuous fermentation'))
print('The productiovity in batch fermentation is', fermentation('Batch fermentation'))
print(f'My favourite process is {process}.')


# Define a function regarding a tuple example
def function(*args):
    print('Number of elements is', len(args))
    for element in args:
        print(element)
function('Aspergillus niger', 'inulinase', 'batch', '1800 U/mL activity')
print()
function('Saccharomyces cerevisia', 'ethanol', 'continuous', '45% yield', 'carob')


# Another example regarding 'args'
def total(*args):
    total = 0
    for i in args:
        total += i
    return total
print('The total of the numbers is', total(0.577, 2.718, 3.14, 1.618, 1729, 6, 37))




# Define a function regarding a dictionary example
def function(**args):
    for key in args:
        print(key, ':', args[key])
function(Micoorganism='Aspergillus niger', Substrate='Molasses', Product='Inulinase', Fermentation_mode='Batch', A



# Define a function regarding the addition of elements into a list
def addition(nlist):
    nlist.append(3.14)
    nlist.append(1.618)
    nlist.append(1729)
    nlist.append(6)
    nlist.append(37)
my_list= [0.577, 2.718]
addition(my_list)
print(my_list)
print(sum(my_list))
print(min(my_list))
print(max(my_list))
print(len(my_list))


# Define a function
def addition(x, y):
    """The following function returns the sum of two parameters."""
    z = x+y
    return z
print(addition.__doc__)
print(addition(3.14, 2.718))



# Calculating the factorial of a certain number.
def factorial(number):
    if number == 0:
        return 1
    else:
    return number*factorial(number-1)
print('The value is', factorial(6))



# Define a function that gives the total of the first ten numbers
def total_numbers(number, sum):
    if number == 11:
        return sum
    else:
    return total_numbers(number+1, sum+number)
print('The total of first ten numbers is', total_numbers(1, 0))




# Define a function that add a number to another number
def added_num(num1):
    def incremented_num(num1):
        num1 = num1 + 1
    return num1
    num2 = incremented_num(num1)
    print(num1, '------->>', num2)
added_num(25)



# Define a function regarding 'nonlocal' function
def print_year():
    year = 1990
    def print_current_year():
        nonlocal year
    year += 32
    print('Current year is', year)
    print_current_year()
print_year()



# Define a function giving a message
def function(name):
    msg = 'Hi ' + name
    return msg
name = input('Enter a name: ')
print(function(name))
