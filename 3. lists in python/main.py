# creatinng a list
nlis = ['python', 25, 2022]
nlis


print('Positive and negative indexing of the first element: \n - Positive index:', nlis[0], '\n - Negative index:', nlis[-3])
print()
print('Positive and negative indexing of the second element: \n - Positive index:', nlis[1], '\n - Negative index:', nlis[-2])
print()
print('Positive and negative indexing of the third element: \n - Positive index:', nlis[2], '\n - Negative index:', nlis[-1])


nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
nlis


# take a list
nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
nlis



# length of the list
len(nlis)


# slicing of a list
print(nlis[0:2])
print(nlis[2:4])
print(nlis[4:6])


# take a list
nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
nlis.extend(['hello world!', 1.618])
nlis


nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
nlis.append(['hello world!', 1.618])
nlis


lis = [1,2,3,4,5,6,7]
print(len(lis))
lis.append(4)
print(lis)
print(lis.count(4)) # How many 4 are on the list 'lis'?
print(lis.index(2)) # What is the index of the number 2 in the list 'lis'?
lis.insert(8, 9) # Add number 9 to the index 8.
print(lis)
print(max(lis)) # What is the maximum number in the list?
print(min(lis)) # What is the minimum number in the list?
print(sum(lis)) # What is the sum of the numbers in the list?



nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
print('Before changing:', nlis)
nlis[0] = 'hello python!'
print('After changing:', nlis)
nlis[1] = 1.618
print('After changing:', nlis)
nlis[2] = [3.14, 2022]
print('After changing:', nlis)



print('Before changing:', nlis)
del(nlis[0])
print('After changing:', nlis)
del(nlis[-1])
print('After changing:', nlis)



nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
print('Before deleting:', nlis)
del nlis
print('After deleting:', nlis)


message = 'Python is a programming language.'
message.split()



text = 'p,y,t,h,o,n'
text.split("," )



nlis_1 = ['a', 'b', 'hello', 'Python']
nlis_2 = [1,2,3,4, 5, 6]
print(len(nlis_1))
print(len(nlis_2))
print(nlis_1+nlis_2)
print(nlis_1*3)
print(nlis_2*3)
for i in nlis_1:
    print(i)
for i in nlis_2:
    print(i)
print(4 in nlis_1)
print(4 in nlis_2)


nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
copy_list = nlis
print('nlis:', nlis)
print('copy_list:', copy_list)



# The element in the copied list also changes when the element in the original list was changed.
# See the following example
nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
print(nlis)
copy_list = nlis
print(copy_list)
print('copy_list[0]:', copy_list[0])
nlis[0] = 'hello python!'
print('copy_list[0]:', copy_list[0])



# The cloned list is a new copy or clone of the original list.
nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
clone_lis = nlis[:]
clone_lis




# When an element in the original list is changed, the element in the cloned list does not change.
nlis = ['python', 3.14, 2022, [1, 1, 2, 3, 5, 8, 13, 21, 34], ('hello', 'python', 3,14, 2022)]
print(nlis)
clone_list = nlis[:]
print(clone_list)
print('clone_list[0]:', clone_list[0])
nlis[0] = 'hello, python!'
print('nlis[0]:', nlis[0])



a_list = ['a', 'b', ['c', 'd'], 'e']
b_list = [1,2,3,4,5,(6,7), True, False]
new_list = a_list + b_list
print(new_list)



text = input('Enter a string:')
print('The text is', text)
print(type(text))


# Although the function wants an integer, the type of the entered number is a string.
number = input('Enter an integer: ')
print('The number is', number)
print(type(number))


number = int(input('Enter an integer:'))
print('The number is', number)
print(type(number))


number = float(input('Enter an integer:'))
print('The number is', number)
print(type(number))


expression = '8+7'
total = eval(expression)
print('Sum of the expression is', total)
print(type(expression))
print(type(total))


a = float(input('Enter the pi number:'))
b = float(input('Enter the golden ratio:'))
total = a + b
print('Sum of {} and {} is {}.'.format(a, b, total))



a = input('Enter your favorite fruit:')
b = input('Enter your favorite food:')
print('I like {} and {}.'.format(a, b))
print('I like {0} and {1}.'.format(a, b))
print('I like {1} and {0}.'.format(a, b))



a = 3.14
b = 1.618
print('a>b is:', a>b)
print('a<b is:', a<b)
print('a<=b is:', a<=b)
print('a>=b is:', a>=b)
print('a==b is:', a==b)
print('a!=b is:', a!=b)



a = 3.14
b = 1.618
c = 12
d = 3.14
print(a>b and c>a)
print(b>c and d>a)
print(b<c or d>a)
print( not a==b)
print(not a==d)


x = 3.14
x+=5
print(x)


x = 3.14
x*=5
print(x)


x = 3.14
x-=5
print(x)


x = 3.14
x/=5
print(x)


x = 3.14
x%=5
print(x)


x = 3.14
x//=5
print(x)


x = 3.14
x**=5
print(x)


a = 3.14
b = 1.618
print(a is b)
print(a is not b)
msg1= 'Hello, Python!'
msg2 = 'Hello, World!'
print(msg1 is msg2)
print(msg1 is not msg2)
lis1 = [3.14, 1.618]
lis2 = [3.14, 1.618]
print(lis1 is lis2) # You should see a list copy behavior
print(lis1 is not lis2)



# take a list
nlis = [4, 6, 7, 8, 'hello', (4,5), {'name': 'Python'}, {1,2,3}, [1,2,3]]
print(5 in nlis)
print(4 not in nlis)
print((4,5) in nlis)
print(9 not in nlis)

