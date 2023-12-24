# Import the module
import array as arr
from array import *


# To access more information regarding array, you can execute the following commands
help(arr)



special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
for i in special_nums:
    print(i)



special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
print(f'First element of numbers is {special_nums[0]}, called euler constant.')
print(f'Second element of numbers is {special_nums[1]}, called golden_ratio.')
print(f'Last element of numbers is {special_nums[-1]}, called Ramanujan-Hardy number.')



nums = arr.array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
# Changing the first element of the array
nums[0] = 55
print(nums)
# Changing 2nd to 4th elements of the array
nums[1:4] =arr.array('i', [89, 144, 233, 377])
print(nums)


nums = arr.array('i', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
# Deleting the first element of the array
del nums[0]
print(nums)
# Deleting the 2nd to 4th elements of the array
del nums[1:4]
print(nums)



special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
print(f'The length of the array is {len(special_nums)}.')



special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
fibonacci_nums = arr.array('d', [1, 1, 2, 3, 5, 8, 13, 21, 34])
special_fibonacci_nums = arr.array('d')
special_fibonacci_nums = special_nums + fibonacci_nums
print(f'The new array called special_fibonacci_nums is {special_fibonacci_nums}.')


mult = 10
one_array = [1]*mult
print(one_array)


mult = 10
nums_array = [i for i in range(mult)]
print(nums_array)




# Using the function 'insert()'
fibonacci_nums = arr.array('i', [1, 1, 2, 3, 5, 8, 13, 21, 34])
print('Before any additon into fibonacci numbers')
for i in fibonacci_nums:
    print(i, end = ' ')
print()
print('After an element additon into fibonacci numbers')
added_num = fibonacci_nums[-1] + fibonacci_nums[-2]
fibonacci_nums.insert(9, added_num)
for i in fibonacci_nums:
    print(i, end = ' ')
print()
print('After an element additon into fibonacci numbers')
added_num = fibonacci_nums[-1] + fibonacci_nums[-2]
fibonacci_nums.insert(10, added_num)
for i in fibonacci_nums:
    print(i, end = ' ')





# Using the function 'append()'
fibonacci_nums = arr.array('i', [1, 1, 2, 3, 5, 8, 13, 21, 34])
print('Before any additon into fibonacci numbers')
for i in fibonacci_nums:
    print(i, end = ' ')
print()
print('After an element additon into fibonacci numbers')
added_num = fibonacci_nums[-1] + fibonacci_nums[-2]
fibonacci_nums.append(added_num)
for i in fibonacci_nums:
    print(i, end = ' ')
print()
print('After an element additon into fibonacci numbers')
added_num = fibonacci_nums[-1] + fibonacci_nums[-2]
fibonacci_nums.append(added_num)
for i in fibonacci_nums:
    print(i, end = ' ')







# Using the function 'remove()'
special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
print('Before removing an element from the array')
for i in special_nums:
    print(i, end = ' ')
print()
print('After removing an element from the array')
special_nums.remove(0.577)
for i in special_nums:
    print(i, end=' ')
print()
print('After removing one more element from the array')
special_nums.remove(special_nums[0]) # We can make this using indexing
for i in special_nums:
    print(i, end=' ')





# Using the function 'pop()'
# The function pop() removes the last element from the array
special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
print('Before removing an element from the array')
for i in special_nums:
    print(i, end = ' ')
print()
print('After removing last element from the array')
special_nums.pop()
for i in special_nums:
    print(i, end=' ')
print()
print('After removing one more last element from the array')
special_nums.pop()
for i in special_nums:
    print(i, end=' ')
print()
print('After removing one more element using index from the array')
special_nums.pop(3) # It deleted the pi number
for i in special_nums:
    print(i, end=' ')
print()







special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
sliced_special_nums = special_nums[1:5] # It returns between index 1 and index 4, not index 5.
print(sliced_special_nums)
# or using for loop
for i in sliced_special_nums:
    print(i, end = " ")



    special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
sliced_special_nums = special_nums[3:] # It returns index 3 and later.
print(sliced_special_nums)



special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
sliced_special_nums = special_nums[:3] # It returns until index 2, not index 3.
print(sliced_special_nums)



special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
sliced_special_nums = special_nums[:] # It returns all elements in the array
print(sliced_special_nums)



special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
sliced_special_nums = special_nums[::-1] # It reverses the array.
print(sliced_special_nums)



# To make a search in an array, use the function index()
special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
searched_item = special_nums.index(2.718)
print(f'The searched item euler number 2.718 is present at index {searched_item}.')
# printing with format
print('The searched item euler number {} is present at index {}.'.format(2.718, searched_item))




special_nums = arr.array('d', [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
copied_special_nums = special_nums
print(special_nums, 'with the ID number', id(special_nums))
print(copied_special_nums, 'with the ID number', id(copied_special_nums))
# Using for loop
for i in special_nums:
    print(i, end= ' ')
print()
print(f'The ID number of the array special_nums is {id(special_nums)}.')
for i in copied_special_nums:
    print(i, end= ' ')
print()
print(f'The ID number of the array copied_special_nums is {id(copied_special_nums)}.')





# import numpy library
import numpy as np
# Copying the array
special_nums = np.array( [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
copied_special_nums = special_nums.view()
print(special_nums, 'with the ID number', id(special_nums))
print(copied_special_nums, 'with the ID number', id(copied_special_nums))
#Using for loop
for i in special_nums:
    print(i, end = ' ')
print()
for i in copied_special_nums:
    print(i, end = ' ')






# import numpy library
import numpy as np
# Copying the array
special_nums = np.array( [0.577, 1.618, 2.718, 3.14, 6, 37, 1729])
copied_special_nums = special_nums.copy()
print(special_nums, 'with the ID number', id(special_nums))
print(copied_special_nums, 'with the ID number', id(copied_special_nums))
#Using for loop
for i in special_nums:
    print(i, end = ' ')
print()
for i in copied_special_nums:
    print(i, end = ' ')






