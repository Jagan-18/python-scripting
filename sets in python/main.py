# The empty set of curly braces denotes the empty dictionary, not empty set
x = {}
print(type(x))


# To take a set without elements, use set() function without any items
y = set()
print(type(y))



# Take a set
set1 = {'Hello Python!', 3.14, 1.618, 'Hello World!', 3.14, 1.618, True, False, 2022}
set1


# A list can convert to a set
# Take a list
nlis = ['Hello Python!', 3.14, 1.618, 'Hello World!', 3.14, 1.618, True, False, 2022]
# Convert the list to a set
set2 = set(nlis)
set2



# Take a set
set3 = set(['Hello Python!', 3.14, 1.618, 'Hello World!', 3.14, 1.618, True, False, 2022])
set3


# Addition of an element to a set
set3 = set(['Hello Python!', 3.14, 1.618, 'Hello World!', 3.14, 1.618, True, False, 2022])
set3.add('Hi, Python!')
set3



# Addition of the same element
set3.add('Hi, Python!')
set3
# As you see that there is only one from the added element 'Hi, Python!'



x_set = {6,7,8,9}
print(x_set)
x_set.update({3,4,5})
print(x_set)


set3.remove('Hello Python!')
set3


set3.discard(3.14)
set3


# To verify if the element is in the set
1.618 in set3


# Take two sets
set4 = set(['Hello Python!', 3.14, 1.618, 'Hello World!'])
set5 = set([3.14, 1.618, True, False, 2022])
# Printing two sets
set4, set5


intersection = set4 & set5
intersection


set4.intersection(set5) # The output is the same as that of above


print(set4.difference(set5))
print(set5.difference(set4))
# The same process can make using subtraction operator as follows:
print(set4-set5)
print(set5-set4)


print(set4>set5)
print(set5>set4)
print(set4==set5)


set4.union(set5)



set(set4).issuperset(set5)



set(set4).issubset(set5)


print(set([3.14, 1.618]).issubset(set5))
print(set([3.14, 1.618]).issubset(set4))
print(set4.issuperset([3.14, 1.618]))
print(set5.issuperset([3.14, 1.618]))


A = [1,1,2,2,3,3,4,4,5,5] # Take a list
B = {1,1,2,2,3,3,4,4,5,5} # Take a set
print('The minimum number of A is', min(A))
print('The minimum number of B is', min(B))
print('The maximum number of A is', max(A))
print('The maximum number of B is', max(B))
print('The sum of A is', sum(A))
print('The sum of B is', sum(B))
# As you see that the sum of A and B is different. Because the set takes no duplicate


set6 = {'Python', 1,2,3, [1,2,3]}
set6


set7 = {1,2,3,4}
set7[1]


set8 = {1,3,5,7,9}
print(set8)
set9 = set8
print(set9)
set8.add(11)
print(set8)
print(set9)
"""
As you see that although the number 8 is added into the set 'set8', the added number
is also added into the set 'set9'
"""



set8 = {1,3,5,7,9}
print(set8)
set9 = set8.copy()
print(set9)
set8.add(11)
print(set8)
print(set9)
"""
When this function is used, the original set stays unmodified.
A new copy stored in another set of memory locations is created.
The change made in one copy won't reflect in another.
"""



x = {0, 1,1,2,3,5,8,13, 21,34}
print( x)
x.clear()
print(x)


x = {0, 1,1,2,3,5,8,13,21,34}
print(x)
x.pop()
print(x)



