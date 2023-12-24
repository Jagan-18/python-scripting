# Take a tuple
tuple_1 = ('Hello', 'Python', 3.14, 1.618, True, False, 32, [1,2,3], {1,2,3}, {'A': 3, 'B': 8}, (0, 1))
tuple_1


print(type(tuple_1))
print(len(tuple_1))


# Printing the each value in a tuple using both positive and negative indexing
tuple_1 = ('Hello', 'Python', 3.14, 1.618, True, False, 32, [1,2,3], {1,2,3}, {'A': 3, 'B': 8}, (0, 1))
print(tuple_1[0])
print(tuple_1[1])
print(tuple_1[2])
print(tuple_1[-1])
print(tuple_1[-2])
print(tuple_1[-3])


# Printing the type of each value in the tuple
tuple_1 = ('Hello', 'Python', 3.14, 1.618, True, False, 32, [1,2,3], {1,2,3}, {'A': 3, 'B': 8}, (0, 1))
print(type(tuple_1[0]))
print(type(tuple_1[2]))
print(type(tuple_1[4]))
print(type(tuple_1[6]))
print(type(tuple_1[7]))
print(type(tuple_1[8]))
print(type(tuple_1[9]))
print(type(tuple_1[10]))


tuple_2 = tuple_1 + ('Hello World!', 2022)
tuple_2


rep_tup = (1,2,3,4)
print(2 in rep_tup)
print(2 not in rep_tup)
print(5 in rep_tup)
print(5 not in rep_tup)


rep_tup = (1,2,3,4)
for i in rep_tup:
    print(i)


def cmp(t1, t2):
    return bool(t1 > t2) - bool(t1 < t2)
def cmp(t31, t4):
    return bool(t3 > t4) - bool(t3 < t4)
def cmp(t5, t6):
    return bool(t5 > t6) - bool(t5 < t6)
t1 = (1,3,5) # Here t1 is lower than t2, since the output is -1
t2 = (2,4,6)
t3 = (5,) # Here t3 is higher than t4 since the output is 1
t4 = (4,)
t5 = (3.14,) # Here t5 is equal to t6 since the output is 0
t6 = (3.14,)
print(cmp(t1, t2))
print(cmp(t3, t4))
print(cmp(t5, t6))



rep_tup = (1,2,3,4)
min(rep_tup)


rep_tup = (1,2,3,4)
max(rep_tup)


seq = 'ATGCGTATTGCCAT'
tuple(seq)


# Obtaining a new tuple from the index 2 to index 6
tuple_1 = ('Hello', 'Python', 3.14, 1.618, True, False, 32, [1,2,3], {1,2,3}, {'A': 3, 'B': 8}, (0, 1))
tuple_1[2:7]



# Obtaining tuple using negative indexing
tuple_1 = ('Hello', 'Python', 3.14, 1.618, True, False, 32, [1,2,3], {1,2,3}, {'A': 3, 'B': 8}, (0, 1))
tuple_1[-4:-1]


tuple_1 = ('Hello', 'Python', 3.14, 1.618, True, False, 32, [1,2,3], {1,2,3}, {'A': 3, 'B': 8}, (0, 1))
len(tuple_1)


# Tuples can be sorted and save as a new tuple.
tuple_3 = (0,9,7,4,6,2,9,8,3,1)
sorted_tuple_3 = sorted(tuple_3)
sorted_tuple_3


# Take a nested tuple
nested_tuple =('biotechnology', (0, 5), ('fermentation', 'ethanol'), (3.14, 'pi', (1.618, 'golden ratio')) )
nested_tuple


# Now printing the each element of the nested tuple
print('Item 0 of nested tuple is', nested_tuple[0])
print('Item 1 of nested tuple is', nested_tuple[1])
print('Item 2 of nested tuple is', nested_tuple[2])
print('Item 3 of nested tuple is', nested_tuple[3])



# Using second index to access other tuples in the nested tuple
print('Item 1, 0 of the nested tuple is', nested_tuple[1][0])
print('Item 1, 1 of the nested tuple is', nested_tuple[1][1])
print('Item 2, 0 of the nested tuple is', nested_tuple[2][0])
print('Item 2, 1 of the nested tuple is', nested_tuple[2][1])
print('Item 3, 0 of the nested tuple is', nested_tuple[3][0])
print('Item 3, 1 of the nested tuple is', nested_tuple[3][1])
print('Item 3, 2 of the nested tuple is', nested_tuple[3][2])
# Accesing to the items in the second nested tuples using a third index
print('Item 3, 2, 0 of the nested tuple is', nested_tuple[3][2][0])
print('Item 3, 2, 1 of the nested tuple is', nested_tuple[3][2][1])



# Take a tuple
tuple_4 = (1,3,5,7,8)
tuple_4[0] = 9
print(tuple_4)
# The output shows the tuple is immutable


tuple_4 = (1,3,5,7,8)
print('Before deleting:', tuple_4)
del tuple_4
print('After deleting:', tuple_4)


tuple_5 = (1,1,3,3,5,5,5,5,6,6,7,8,9)
tuple_5.count(5)


tuple_5 = (1,1,3,3,5,5,5,5,6,6,7,8,9)
print(tuple_5.index(5))
print(tuple_5.index(1))
print(tuple_5.index(9))


tuple_6 = (0)
print(tuple_6)
print(type(tuple_6))
# Here, you see that the output is an integer


tuple_7 = (0,)
print(tuple_7)
print(type(tuple_7))
# You see that the output is a tuple




