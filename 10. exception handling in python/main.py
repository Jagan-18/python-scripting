# If a number is divided by 0, it gives a ZeroDivisionError.
try:
    1/0
except ZeroDivisionError:
    print('This code gives a ZeroDivisionError.')
print(1/0)



nlis = []
count = 0
try:
    mean = count/len(nlis)
    print('The mean value is', mean)
except ZeroDivisionError:
    print('This code gives a ZeroDivisionError')
print(count/len(nlis))



# The following code is like 1/0.
try:
    True/False
except ZeroDivisionError:
    print('The code gives a ZeroDivisionError.')
print(True/False)



nlis = []
count = 0
try:
    mean = count/len(nlis)
    print('The mean value is', mean)
except ZeroDivisionError:
    print('This code gives a ZeroDivisionError')
# Since the variable 'mean' is not defined, it gives us a 'NameError
print(mean)



try:
    y = x+5
except NameError:
    print('This code gives a NameError.')
print(y)



# Define a function giving a NameError
def addition(x, y):
    z = x + y
    return z
print('This function gives a NameError.')
total = add(3.14, 1.618)
print(total)




# Since 'Mustafa' is not defined, the following code gives us a 'NameError.'
try:
    name = (Mustafa)
    print(name, 'today is your wedding day.')
except NameError:
    print('This code gives a NameError.')
name = (Mustafa)
print(name, 'today is your wedding day.')






nlis = [0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729]
try:
    nlis[10]
except IndexError:
    print('This code gives us a IndexError.')
print(nlis[10])




# You can also supplytake this error type with tuple
tuple_sample = (0.577, 1.618, 2.718, 3.14, 6, 28, 37, 1729)
try:
    tuple_sample[10]
except IndexError:
    print('This code gives us a IndexError.')
print(tuple_sample[10])



dictionary = {'euler_constant': 0.577, 'golden_ratio': 1.618}
try:
    dictonary = dictionary['euler_number']
except KeyError:
    print('This code gives us a KeyError.')
dictonary = dictionary['euler_number']
print(dictonary)




try:
    print(name)
except NameError:
    print('Since the variable name is not defined, the function gives a NameError.')



    num1 = float(input('Enter a number:'))
print('The entered value is', num1)
try:
    num2 = float(input('Enter a number:'))
    print('The entered value is', num2)
    value = num1/num2
    print('This process is running with value = ', value)
except:
    print('This process is not running.')




    num1 = float(input('Enter a number:'))
print('The entered value is', num1)
try:
    num2 = float(input('Enter a number:'))
    print('The entered value is', num2)
    value = num1/num2
    print('This process is running with value = ', value)
except ZeroDivisionError:
    print('This function gives a ZeroDivisionError since a number cannot divide by 0.')
except ValueError:
    print('You should provide a number.')
except:
    print('Soething went wrong!')




    num1 = float(input('Enter a number:'))
print('The entered value is', num1)
try:
    num2 = float(input('Enter a number:'))
    print('The entered value is', num2)
    value = num1/num2
except ZeroDivisionError:
    print('This function gives a ZeroDivisionError since a number cannot divide by 0.')
except ValueError:
    print('You should provide a number.')
except:
    print('Soething went wrong!')
else:
    print('This process is running with value = ', value)




    num1 = float(input('Enter a number:'))
print('The entered value is', num1)
try:
    num2 = float(input('Enter a number:'))
    print('The entered value is', num2)
    value = num1/num2
except ZeroDivisionError:
    print('This function gives a ZeroDivisionError since a number cannot divide by 0.')
except ValueError:
    print('You should provide a number.')
except:
    print('Soething went wrong!')
else:
    print('This process is running with value = ', value)
finally:
    print('The process is completed.')




    num1 = float(input('Enter a number:'))
print('The entered value is', num1)
try:
    num2 = float(input('Enter a number:'))
    print('The entered value is', num2)
    value = num1/num2
except (ZeroDivisionError, NameError, ValueError): #Multiple except clauses
    print('This function gives a ZeroDivisionError, NameError or ValueError.')
except:
    print('Soething went wrong!')
else:
    print('This process is running with value = ', value)
finally:
    print('The process is completed.')





num = int(input('Enter a number:'))
print('The entered value is', num)
try:
    if num>1000 and num %2 == 0 or num %2 !=0:
        raise Exception('Do not allow to the even numbers higher than 1000.')
except:
    print('Even or odd numbers higher than 1000 are not allowed!')
else:
    print('This process is running with value = ', num)
finally:
    print('The process is completed.')




