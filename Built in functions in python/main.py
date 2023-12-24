num1 = int(input('Enter a number: '))
print('The entered number is', num1)
num2 = float(input('Enter a number: '))
print('The entered number is', num2)
print('The absolute value of the first number is', abs(num1))
print('The absolute number of the second number is', abs(num2))
print('The difference between the two numbers is', abs(num1-num2))



nlis1 = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(all(nlis1))
nlis1.append(0) # Add '0' to the end of the list
print(nlis1)
print(all(nlis1))
nlis1.append(False) # Adds 'False' to the end of the list
print(nlis1)
print(all(nlis1))
nlis1.clear() # It returns an emtpy list
print(nlis1)
print(all(nlis1))



num = int(input('Enter a number: '))
print(f'The entered number is {num}.')
print(f'The binary representation of {num} is {bin(num)}.')



lis, dict, tuple = [], {}, ()
print(bool(lis), bool(dict), bool(tuple))
lis, dict, tuple = [0], {'a': 1}, (1,)
print(bool(lis), bool(dict), bool(tuple))
lis, dict, tuple = [0.0], {'a': 1.0}, (1.0,)
print(bool(lis), bool(dict), bool(tuple))
a, b, c = 0, 3.14, 'Hello, Python!'
print(bool(a), bool(b), bool(c))
statement = None
print(bool(None))
true = True
print(bool(true))




msg = 'Hello, Python!'
new_msg = bytes(msg, 'utf-8')
print(new_msg)
var = 3.14



print(callable(var)) # since the object does not appear callable, it returns False
def function(): # since the object appears callable, it returns True
    print('Hi, Python!')
msg = function
print(callable(msg))



print(chr(66))
print(chr(89))
print(chr(132))
print(chr(1500))
print(chr(3))
print(chr(-500)) # The argument must be inside of the range.


print(chr('Python')) # The argument maut be integer.



code_line = 'x=3.14\ny=2.718\nprint("Result =", 2*x+5*y)'
code = compile(code_line, 'Result.py', 'exec')
print(type(code))
exec(code)


var = 3.14
exec('print(var==3.14)')
exec('print(var!=3.14)')
exec('print(var+2.718)')



class SpecialNumbers:
    euler_constant = 0.577
    euler_number = 2.718
    pi = 3.14
    golden_ratio = 1.618
    msg = 'These numbers are special.'
special_numbers = SpecialNumbers()
print('The euler number is', getattr(special_numbers, 'euler_number'))
print('The golden ratio is', special_numbers.golden_ratio)



class SpecialNumbers:
    euler_constant = 0.577
    euler_number = 2.718
    pi = 3.14
    golden_ratio = 1.618
    msg = 'These numbers are special.'

    def parameter(self):
        print(self.euler_constant, self.euler_number, self.pi, self.golden_ratio, self.msg)
special_numbers = SpecialNumbers()
special_numbers.parameter()
delattr(SpecialNumbers, 'msg') # The code deleted the 'msg'.
special_numbers.parameter() # Since the code deleted the 'msg', it returns an AttributeError.


name = dict()
print(name)
dictionary = dict(euler_constant = 0.577, euler_number=2.718, golden_ratio=1.618)
print(dictionary)


str_list = ['Hello Python!','Hello, World!']
for i, str_list in enumerate(str_list):
    print(i, str_list)


    str_list = ['Hello Python!','Hello, World!']
enumerate_list = enumerate(str_list)
print(list(enumerate_list))



def filtering(data):
    if data > 30:
        return data
data = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
result = filter(filtering, data)
print(list(result))



globals()



num = 37
globals()['num'] = 3.14
print(f'The number is {num}.')



nlis = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
frozen_nlis = frozenset(nlis)
print('Frozen set is', frozen_nlis)


nlis = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(nlis)
print(any(nlis))
nlis.clear()
print(nlis)
print(any(nlis)) # An emptly list returns False
nlis.append(0)
print(nlis)
print(any(nlis)) # 0 in a list returns False
nlis.append(False)
print(nlis)
print(any(nlis)) # False in a list returns False
nlis.append(True)
print(nlis)
print(any(nlis)) # True in a list returns True
nlis.append(1)
print(nlis)
print(any(nlis)) # 1 in a list returns True
nlis.clear()
nlis.append(None)
print(nlis)
print(any(nlis)) # None in a list returns False



txt = 'Hello, Python!'
print(ascii(txt))
text = 'Hello, Pythän!'
print(ascii(text))
print('Hello, Pyth\xe4n!')
msg = 'Hellü, World!'
print(ascii(msg))
print('Hell\xfc, World!')



txt = 'Hello, Python!'
print(bytearray(txt, 'utf-8')) # String with encoding 'UTF-8'
int_num = 37
print(bytearray(int_num))
nlis = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] # Fibonacci numbers
print(bytearray(nlis))
float_num = 3.14
print(bytearray(float_num)) # It returns TypeError



class SpecialNumbers:
    euler_constant = 0.577
    euler_number = 2.718
    pi = 3.14
    golden_ratio = 1.618
    msg = 'These numbers are special.'
special_numbers = SpecialNumbers()
print('The euler number is', hasattr(special_numbers, 'euler_number'))
print('The golden ratio is', hasattr(special_numbers, 'golden_ratio'))
print('The golden ratio is', hasattr(special_numbers, 'prime_number')) # Since there is no prime number, the output


print(hash(3.14))
print(hash(0.577))
print(hash('Hello, Python!'))
print(hash(1729))
n_tuple = (0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729)
print(hash(n_tuple))



help()



import pandas as pd
help(pd) # You can find more information about pandas.





print(id('Hello, Python!'))
print(id(3.14))
print(id(1729))
special_nums_list = [0.577, 1.618, 2.718, 3.14, 28, 37, 1729]
print(id(special_nums_list))
special_nums_tuple = (0.577, 1.618, 2.718, 3.14, 28, 37, 1729)
print(id(special_nums_tuple))
special_nums_set = {0.577, 1.618, 2.718, 3.14, 28, 37, 1729}
print(id(special_nums_set))
special_nums_dict = {'Euler constant': 0.577, 'Golden ratio': 1.618,
                     'Euler number': 2.718, 'PI number': 3.14,
                     'Perfect number': 28, 'Prime number': 37,
                     'Ramanujan Hardy number': 1729}
print(id(special_nums_dict))



num = int(input('Enter a number: '))
print(f'The entered number is {num}.')
print(eval('num*num'))



special_nums = [0.577, 1.618, 2.718, 3.14, 28, 37, 1729]
def division(number):
    return number/number
division_number_iterator = map(division, special_nums)
divided_nums = list(division_number_iterator)
print(divided_nums)
# Similar codings can be made for other operations


special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print('The length of the list is', len(special_nums))



# Calculate the average of values in the following list
special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
count = 0
for i in special_nums:
    count = count + i
print('The average of the values in the list is', count/len(special_nums))


special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(min(special_nums)



special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(max(special_nums))



special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(sum(special_nums))


int_num = 37
print(float(int_num))
float_num = 3.14
print(float(float_num))
txt = '2.718'
print(float(txt))
msg = 'Hello, Python!' # It resturns a ValueError
print(float(msg))



locals()



def function():
    variable = True
    print(variable)
    locals()['variable'] = False # locals() dictionary may not change the information inside the locals table.
    print(variable)
function()



def dict_1():
    return locals()
def dict_2():
    program = 'Python'
    return locals()
print('If there is no locals(), it returns an empty dictionary', dict_1())
print('If there is locals(), it returns a dictionary', dict_2())



# integer format
int_num = 37
print(format(num, 'd'))
# float numbers
float_num = 2.7182818284
print(format(float_num, 'f'))
# binary format
num = 1729
print(format(num, 'b'))



print(hex(6))
print(hex(37))
print(hex(1729))


txt = input('Enter a message: ')
print('The entered message is', txt)


num1 = int(6)
num2 = int(3.14)
num3 = int('28')
print(f'The numbers are {num1}, {num2},and {num3}.')


special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
result = isinstance(special_nums, list)
print(result)



class SpecialNumbers:
    euler_constant = 0.577
    euler_number = 2.718
    pi = 3.14
    golden_ratio = 1.618
    msg = 'These numbers are very special'

    def __init__(self, euler_constant, euler_number, pi, golden_ratio, msg):
        self.euler_constant = euler_constant
    self.euler_number = euler_number
    self.pi = pi
    self.golden_ratio = golden_ratio
    self.msg = msg
special_numbers = SpecialNumbers(0.577, 2.718, 3.14, 1.618, 'These numbers are very special.')
nums = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
print(isinstance(special_numbers, SpecialNumbers))
print(isinstance(nums, SpecialNumbers))


class Circle:
    def __init__(circleType):
        print('Circle is a ', circleType)

class Square(Circle):
    def __init__(self):

    Circle.__init__('square')

print(issubclass(Square, Circle))
print(issubclass(Square, list))
print(issubclass(Square, (list, Circle)))
print(issubclass(Circle, (list, Circle)))



special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
special_nums_iter = iter(special_nums)
print('Euler constant is', next(special_nums_iter))
print('The golden ratio is', next(special_nums_iter))
print('Euler number is', next(special_nums_iter))
print('Pi number is', next(special_nums_iter))
print(next(special_nums_iter), 'is a perfect number.')
print(next(special_nums_iter), 'is a perfect number.')
print(next(special_nums_iter), 'is a special and prime number.')
print(next(special_nums_iter), 'is Ramanujan-Hardy number.')



name= object()
print(type(name))
print(dir(name))




num = int(input('Enter a number:'))
print(f'The octal value of {num} us {oct(num)}.')


# decimal to octal
print('oct(1729) is:', oct(1729))
# binary to octal
print('oct(0b101) is:', oct(0b101))
# hexadecimal to octal
print('oct(0XA) is:', oct(0XA))



print(list())
txt = 'Python'
print(list(txt))
special_nums_set = {0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729}
print(list(special_nums_set))
special_nums_tuple = (0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729)
print(list(special_nums_tuple))
special_nums_dict = {'Euler constant': 0.577,
                     'Golden ratio': 1.618,
                     'Euler number': 2.718,
                     'Pi number': 3.14,
                     'Perfect number': 6,
                     'Prime number': 37,
                     'Ramanujan Hardy number': 1729}
print(list(special_nums_dict))



ba = bytearray('XYZ', 'utf-8')
mv = memoryview(ba)
print(mv)
print(mv[0])
print(mv[1])
print(mv[2])
print(bytes(mv[0:2]))
print(list(mv[:]))
print(set(mv[:]))
print(tuple(mv[:]))
mv[1] = 65 # 'Y' was replaced with 'A'
print(list(mv[:]))
print(ba)



special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
number = iter(special_nums) # Create an iteration
item = next(number) # First item
print(item)
item = next(number) # Second item
print(item)
item = next(number) # Third item, etc
print(item)
item = next(number)
print(item)
item = next(number)
print(item)
item = next(number)
print(item)
item = next(number)
print(item)
item = next(number)
print(item)



path = "authors.txt"
file = open(path, mode = 'r', encoding='utf-8')
print(file.name)
print(file.read())


# Open file using with
path = "authors.txt"
with open(path, "r") as file:
    FileContent = file.read()
    print(FileContent)



print(complex(1))
print(complex(2, 2))
print(complex(3.14, 1.618))



name = dir()
print(name)
print()
number = 3.14
print(dir(number))
print()
nlis = [3.14]
print(dir(nlis))
print()
nset = {3.14}
print(dir(nset))



print(divmod(3.14, 0.577))
print(divmod(9, 3))
print(divmod(12, 5))
print(divmod('Hello', 'Python!')) # It returns TypeError.



print(set())
print(set('3.15'))
print(set('Hello Python!'))
special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
print(set(special_nums))
print(set(range(2, 9)))
special_nums_dict = {'Euler constant': 0.577, 'Golden ratio': 1.618, 'Euler number': 2.718, 'Pi number': 3.14, 'Perfect n
    print(set(special_nums_dict))



class SpecialNumbers:
    euler_constant = 0.0
    euler_number = 0.0
    pi = 0.0
    golden_ratio = 0.0
    msg = ''

    def __init__(self, euler_constant, euler_number, pi, golden_ratio, msg):
        self.euler_constant = euler_constant
    self.euler_number = euler_number
    self.pi = pi
    self.golden_ratio = golden_ratio
    self.msg = msg
special_numbers = SpecialNumbers(0.577, 2.718, 3.14, 1.618, 'These numbers are special.')
print(special_numbers.euler_constant)
print(special_numbers.euler_number)
print(special_numbers.pi)
print(special_numbers.golden_ratio)
print(special_numbers.msg)
setattr(special_numbers, 'Ramanujan_Hardy_number', 1729)
print(special_numbers.Ramanujan_Hardy_number)



print(slice(2.718))
print(slice(0.577, 1.618, 3.14))
msg = 'Hello, Python!'
sliced_msg = slice(5)
print(msg[sliced_msg])
special_nums = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
sliced_list = slice(4)
print(special_nums[sliced_list])
sliced_list = slice(-1, -6, -2)
print(special_nums[sliced_list])
print(special_nums[0:4]) # Slicing with indexing
print(special_nums[-4:-1])


special_nums = [2.718, 1729, 0.577, 1.618, 28, 3.14, 6, 37]
print(sorted(special_nums))
txt = 'Hello, Python!'
print(sorted(txt))


print(ord('9'))
print(ord('X'))
print(ord('W'))
print(ord('^'))


print(pow(2.718, 3.14))
print(pow(-25, -2))
print(pow(16, 3))
print(pow(-6, 2))
print(pow(6, -2))



msg = 'Hello, Python!'
print(msg)


print(list(range(0)))
print(list(range(9)))
print(list(range(2, 9)))
for i in range(2, 9):
    print(i)



txt = 'Python'
print(list(reversed(txt)))
special_nums = [2.718, 1729, 0.577, 1.618, 28, 3.14, 6, 37]
print(list(reversed(special_nums)))
nums = range(6, 28)
print(list(reversed(nums)))
special_nums_tuple = (2.718, 1729, 0.577, 1.618, 28, 3.14, 6, 37)
print(list(reversed(special_nums_tuple)))



print(round(3.14))
print(round(2.718))
print(round(0.577))
print(round(1.618))
print(round(1729))




num = 3.14
val = str(num)
print(val)
print(type(val))


special_nums = [2.718, 1729, 0.577, 1.618, 28, 3.14, 6, 37]
special_nums_tuple = tuple(special_nums)
print(special_nums_tuple)
txt = 'Hello, Python!'
txt_tuple = tuple(txt)
print(txt_tuple)
dictionary = {'A': 0.577, 'B': 2.718, 'C': 3.14}
dictionary_tuple = tuple(dictionary)
print(dictionary_tuple)






special_nums = [2.718, 1729, 0.577, 1.618, 28, 3.14, 6, 37]
special_nums_tuple = tuple(special_nums)
print(special_nums_tuple)
print(type(special_nums))
print()
txt = 'Hello, Python!'
txt_tuple = tuple(txt)
print(txt_tuple)
print(type(txt))
print()
dictionary = {'A': 0.577, 'B': 2.718, 'C': 3.14}
dictionary_tuple = tuple(dictionary)
print(dictionary_tuple)
print(type(dictionary))
print()
special_nums_set = {2.718, 1729, 0.577, 1.618, 28, 3.14, 6, 37}
special_nums_tuple = tuple(special_nums_set)
print(special_nums_tuple)
print(type(special_nums_set))
print()
class SpecialNumbers:
    euler_constant = 0.577
    euler_number = 2.718
    pi = 3.14
    golden_ratio = 1.618
    msg = 'These numbers are very special'

    def __init__(self, euler_constant, euler_number, pi, golden_ratio, msg):
        self.euler_constant = euler_constant
    self.euler_number = euler_number
    self.pi = pi
    self.golden_ratio = golden_ratio
    self.msg = msg
special_numbers = SpecialNumbers(0.577, 2.718, 3.14, 1.618, 'These numbers are very special.')
print(type(special_numbers))





class SpecialNumbers:
    euler_constant = 0.577
    euler_number = 2.718
    pi = 3.14
    golden_ratio = 1.618
    msg = 'These numbers are very special'

    def __init__(self, euler_constant, euler_number, pi, golden_ratio, msg):
        self.euler_constant = euler_constant
    self.euler_number = euler_number
    self.pi = pi
    self.golden_ratio = golden_ratio
    self.msg = msg
special_numbers = SpecialNumbers(0.577, 2.718, 3.14, 1.618, 'These numbers are very special.')
print(vars(special_numbers))




special_nums = [2.718, 1729, 0.577, 1.618, 28, 3.14, 37]
special_nums_name = ['Euler number', 'Ramanujan-Hardy number', 'Euler constant', 'Golden ratio', 'Perfect number',
                     output = zip()
output_list = list(output)
print(output_list)
reel_output = zip(special_nums_name, special_nums)
reel_output_set = set(reel_output)
print(reel_output_set)





class SpecialNumbers(object):
    def __init__(self, special_numbers):
        print('6 and 28 are', special_numbers)
class PerfectNumbers(SpecialNumbers):
    def __init__(self):

    # call superclass
    super().__init__('perfect numbers.')
    print('These numbers are very special in mathematik.')
nums = PerfectNumbers()






class Animal(object):
    def __init__(self, AnimalName):
        print(AnimalName, 'lives in a farm.')

class Cow(Animal):
    def __init__(self):
        print('Cow gives us milk.')
    super().__init__('Cow')

result = Cow()



math = __import__('math', globals(), locals(), [], 0)
print(math.fabs(3.14))
print(math.fabs(-2.718))
print(math.pow(4, 3))
print(math.exp(-5))
print(math.log(2.718))
print(math.factorial(6))




import math
print(math.fabs(3.14))
print(math.fabs(-2.718))
print(math.pow(4, 3))
print(math.exp(-5))
print(math.log(2.718))
print(math.factorial(6))






