# Define a function using 'def'
def f(x):
    return x + 6
print(f(3.14))
# Define the same function using 'lambda'
(lambda x: x+6) (3.14)



# Define a function using 'def'
def f(x, y):
    return x + y

print('The sum of {} and {} is'.format(3.14, 2.718), f(3.14, 2.718))
# Define the same function using 'lambda
print(f'The sum of pi number and euler number is {(lambda x, y: x+y)(3.14, 2.718)}.')




# Calculate the volume of a cube using def and lambda functions
# def function
def cube_volume_def(a):
    return a*a*a
print(f'The volume of a cube using def function is {cube_volume_def(3.14)}.')
# lambda function
print(f'The volume of a cube using lambda function is {(lambda a: a*a*a)(3.14)}.')






def mult_table(n):
    return lambda x:x*n
n = int(input('Enter a number: '))
y = mult_table(n)
print(f'The entered number is {n}.')
for i in range(11):
    print(('%d x %d = %d' %(n, i, y(i))))




# This program returns a new list when the special numbers in the list are divided by 2 and the remainder is equal to 0
special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
list(filter(lambda x:(x%2==0), special_nums))




# This program will multiplicate each element of the list with 5 and followed by power of 2.
special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(f'Non special numbers are {list(map(lambda x: x*5, special_nums))}')
print(f'Non special numbers list is {list(map(lambda x: pow(x, 2), special_nums))}')




nums = [lambda a=a:a+3.14 for a in range(5)]
nlis = []
for num in nums:
    nlis.append(num())
print(nlis)



age = int(input('Enter an age: '))
print(f'The entered age is {age}.')
(lambda age: print('Therefore, you can use a vote.') if (age>=18) else print('Therefore, you do not use a vote.'))(age)



special_nums = [[0.577, 1.618, 2.718, 3.14], [6, 28, 37, 1729]]
special_nums_sorted = lambda a: (sorted(i) for i in a)
# Get the maximum of special numbers in the list
special_nums_max = lambda a, f: [y[len(y)-1] for y in f(a)]
print(f'The maximum of special numbers in each list is {special_nums_max(special_nums, special_nums_sorted)}.')
# Get the minimum of special numbers in the list
special_nums_min = lambda a, f: [y[len(y)-len(y)] for y in f(a)]
print(f'The minimum of special numbers in each list is {special_nums_min(special_nums, special_nums_sorted)}.')
# Get the second maximum of special numbers in the list
special_nums_second_max = lambda a, f: [y[len(y)-2] for y in f(a)]
print(f'The second maximum of special numbers in each list is {special_nums_second_max(special_nums, special_num








def func(n):
    return lambda x: x*n
mult_pi_number = func(3.14)
mult_euler_constant = func(0.577)
print(f'The multiplication of euler number and pi number is equal to {mult_pi_number(2.718)}.')
print(f'The multiplication of euler number and euler constant is equal to {mult_euler_constant(2.718)}.')




text = 'Python is a programming language.'
print(lambda text: text)


text = 'Python is a programming language.'
(lambda text: print(text))(text)



lambda_list = []
# Multiplication of pi number and 12 in one line using lambda function
lambda_list.append((lambda x:x*3.14) (12))
# Division of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x/3.14) (12))
# Addition of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x+3.14) (12))
# Subtraction of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x-3.14) (12))
# Remainder of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x%3.14) (12))
# Floor division of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x//3.14) (12))
# Exponential of pi number and 12 in one line using lambda function
lambda_list.append((lambda x: x**3.14) (12))
# Printing the list
print(lambda_list)



# Using the function reduce() with lambda to get the sum abd average of the list.
# You should import the library 'functools' first.
import functools
from functools import *
special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(f'The sum and average of the numbers in the list are {reduce((lambda a, b: a+b), special_nums)} and {reduce((la





import itertools
from itertools import product
from numpy import sqrt
X=[1]
X1=[2]
Y=[1,2,3]
print(list(product(Y,X,X1)))
print(list(map(lambda x: sqrt(x[1]+x[0]**x[2]),product(Y,X,X1))))




help(functools)



