# Take a range() function
print(range(5))
print(range(10))


# Take an example
# Diectly accessing to the elements in the list
years = [2005, 2006, 2007, 2008, 2009, 2010]
for i in years:
    print(i)


# Again, directly accessing to the elements in the list
years = [2005, 2006, 2007, 2008, 2009, 2010]
for year in years:
    print(year)


    # Take an example
years = [2005, 2006, 2007, 2008, 2009, 2010]
for i in range(len(years)):
    print(years[i])


    # Another for loop example
for i in range(2, 12):
    print(i)


    # Striding in for loop
for i in range(2, 12, 3):
    print(i)


    # Changing the elements in the list
languages = ['Java', 'JavaScript', 'C', 'C++', 'PHP']
for i in range(len(languages)):
    print('Before language', i, 'is', languages[i])
    languages[i] = 'Python'
    print('After language', i, 'is', languages[i])


    # Enumaeration of the elements in the list
languages = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'PHP']
for index, language in enumerate(languages):
    print(index, language)


    # Take the numbers between -3 and 6 using for loop
# Use range() function
for i in range(-3, 7):
    print(i)



# Take a list and print the elements using for loop
languages = ['Python', 'Java', 'JavaScript', 'C', 'C++', 'PHP']
for i in range(len(languages)):
    print(i, languages[i])


number1 = int(input('Enter a number:'))
number2 = int(input('Enter a number:'))
print(f'The entered numbers are {number1} and {number2}.')
for i in range(0, 11):
    print(('%d x %d = %d' %(number1, i, number1*i)), ',', ('%d x %d = %d' %(number2, i, number2*i )))



    # Take a list
nlis = [0.577, 2.718, 3.14, 1.618, 1729, 6, 37]
# Write a for loop for addition
count = 0
for i in nlis:
    count+=i
print('The total value of the numbers in the list is', count)
# Calculate the average using len() function
print('The avearge value of the numbers in the list is', count/len(nlis))



for i in range(1,6):
    print(i, end=", ")
else:
    print('These are numbers from 1 to 5.')



    num = int(input('Enter a number:'))
print(f'The entered the number is {num}.')
i, j = 0, 0
for i in range(0, num):
    print()
    for j in range(0, i+1):
        print('+', end='')




# Take a list
nlis = [1,2,4,5,6,7,8,9,10,11,12,13,14]
for i in nlis:
    if i == 5:
        continue
    print(i)

"""
You see that the output includes the numbers without 5.
The continue function jumps when it meets with the reference.
"""



# Take a list
nlis = [1,2,4,5,6,7,8,9,10,11,12,13,14]
for i in nlis:
    if i == 5:
        break
    print(i)

"""
You see that the output includes the numbers before 5.
The break function terminate the loop when it meets with the reference.
"""



# Take an example
i = 22
while i<27:
    print(i)
    i+=1



    #Take an example
i = 22
while i>=17:
    print(i)
    i-=1



# Take an example
years = [2005, 2006, 2007, 2008, 2009, 2010]
index = 0
year = years[0]
while year !=2008:
    print(year)
    index+=1
    year = years[index]
print('It gives us only', index, 'repetititons to get out of loop')



# Print the movie ratings gretater than 6.
movie_rating = [8.0, 7.5, 5.4, 9.1, 6.3, 6.5, 2.1, 4.8, 3.3]
index = 0
rating = movie_rating[0]
while rating>=6:
    print(rating)
    index += 1
    rating = movie_rating[index]
print('There is only', index, 'movie rating, because the loop stops when it meets with the number lower than 6.')



# Print the movie ratings gretater than 6.
movie_rating = [8.0, 7.5, 5.4, 9.1, 6.3, 6.5, 2.1, 4.8, 3.3]
index = 0
for i in range(len(movie_rating)):
    if movie_rating[i] >= 6:
        index += 1
    print(index, movie_rating[i])
print('There is only', index, 'films gretater than movie rating 6')



# Adding the element in a list to a new list
fruits = ['banana', 'apple', 'banana', 'orange', 'kiwi', 'banana', 'Cherry', 'Grapes']
new_fruits = []
index = 0
while fruits[index] == 'banana':
    new_fruits.append(fruits[index])
    index += 1
print(new_fruits)


number1 = int(input('Enter a number:'))
number2 = int(input('Enter a number:'))
print(f'The entered numbers are {number1} and {number2}.')
i = 0
while i<=10:
    print(('%d x %d = %d' %(number1, i, number1*i)), ',', ('%d x %d = %d' %(number2, i, number2*i )))
    i+=1



index = 0
while index <=5:
    print(index, end=' ')
    index += 1
else:
    print('It gives us the numbers between 0 and 5.')


    i = 0
while i<=5:
    print(i)
    i+=1
    if i == 3:
        continue



i = 0
while i<=5:
    print(i)
    i+=1
    if i == 3:
        break