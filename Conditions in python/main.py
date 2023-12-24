# Take a variable
golden_ratio = 1.618
# Condition less than
print(golden_ratio<2) # The golden ratio is lower than 2, thus the output is True
print(golden_ratio<1) # The golden ratio is greater than 1, thus the output is False


# Take a variable
golden_ratio = 1.618
# Condition less than or equal to
print(golden_ratio<=2) # The golden ratio is lower than 2, thus the condition is True.
print(golden_ratio<=1) # The golden ratio is greater than 1, thus the condition is False.
print(golden_ratio<=1.618) # The golden ratio is equal to 1.618, thus the condition is True.


# Take a variable
golden_ratio = 1.618
# Condition greater than
print(golden_ratio>2) # The golden ratio is lower than 2, thus the condition is False.
print(golden_ratio>1) # The golden ratio is greater than 1, thus the condition is True.


# Take a variable
golden_ratio = 1.618
# Condition greater than or equal to
print(golden_ratio>=2) # The golden ratio is not greater than 2, thus the condition is False.
print(golden_ratio>=1) # The golden ratio is greater than 1, thus the condition is True.
print(golden_ratio>=1.618) # The golden ratio is equal to 1.618, thus the condition is True.


# Take a variable
golden_ratio = 1.618
# Condition equal to
print(golden_ratio==2) # The golden ratio is not equal to 1.618, thus the condition is False.
print(golden_ratio==1.618) # The golden ratio is equal to 1.618, thus the condition is True


# Take a variable
golden_ratio = 1.618
# Condition not equal to
print(golden_ratio!=2) # The golden ratio is not equal to 1.618, thus the condition is True.
print(golden_ratio!=1.618) # The golden ratio is equal to 1.618, thus the condition is False.


# Compare strings
print('Hello' == 'Python')
print('Hello' != 'Python')
print('Hello' <= 'Python')
print('Hello' >= 'Python')
print('Hello' < 'Python')
print('Hello' > 'Python')
print('B'>'A') # According to ASCII table, the values of A and B are equal 65 and 66, respectively.
print('a'>'b') # According to ASCII table, the values of a and b are equal 97 and 98, respectively.
print('CD'>'DC') # According to ASCII table, the value of C (67) is lower than that of D (68)
# The values of uppercase and lowercase letters are different since python is case sensitive.



pi = 3.14
golden_ratio = 1.618
# This statement can be True or False.
if pi > golden_ratio:
    # If the conditions is True, the following statement will be printed.
    print(f'The number pi {pi} is greater than the golden ratio {golden_ratio}.')
# The following statement will be printed in each situtation.
print('Done!')



if 2:
    print('Hello, python!')


    if True:
print('This is true.')


pi = 3.14
golden_ratio = 1.618
if pi < golden_ratio:
    print(f'The number pi {pi} is greater than the golden ratio {golden_ratio}.')
else:
    print(f'The golden ratio {golden_ratio} is lower than the number pi {pi}.')
print('Done!')



age = 5
if age > 6:
    print('You can go to primary school.' )
elif age == 5:
    print('You should go to kindergarten.')
else:
    print('You are a baby' )

print('Done!')



album_year = 2000
album_year = 1990
if album_year >= 1995:
    print('Album year is higher than 1995.')
print('Done!')


album_year = 2000
# album_year = 1990
if album_year >= 1995:
    print('Album year is higher than 1995.')
else:
    print('Album year is lower than 1995.')
print('Done!')



imdb_point = 9.0
if imdb_point > 8.5:
    print('The movie could win Oscar.')


    movie_rating = float(input('Enter a rating number:'))
print(f'The entered movie rating is: {movie_rating}')
if movie_rating > 8.5:
    print('The movie is awesome with {} rating and you should watch it.'.format(movie_rating))
else:
    print('The movie has merit to be watched with {} rating.'.format(movie_rating))


    note = float(input('Enter a note:'))
print(f'The entered note value is: {note}')
if note >= 90 and note <= 100:
    print('The letter grade is AA.')
elif note >= 85 and note <= 89:
    print('The letter grade is BA.')
elif note >= 80 and note <= 84:
    print('The letter grade is BB.')
elif note >= 75 and note <= 79:
    print('The letter grade is CB.')
elif note >= 70 and note <= 74:
    print('The letter grade is CC.')
elif note >= 65 and note <= 69:
    print('The letter grade is DC.')
elif note >= 60 and note <= 64:
    print('The letter grade is DD.')
elif note >=55 and note <= 59:
    print('The letter grade is ED.')
elif note >=50 and note <= 54:
    print('The letter grade is EE.')
elif note >=45 and note <=49:
    print('The letter grade is FE.')
else:
    print('The letter grade is FF.')



number = int(input('Enter a number:'))
print(f'The entered number is: {number}')
if number %2 == 0:
    print(f'The entered number {number} is even')
else:
    print(f'The entered number {number} is odd')



    birth_year = 1990
if birth_year > 1989 and birth_year < 1995:
    print('You were born between 1990 and 1994')
print('Done!')


x = int(input('Enter a number:'))
y = int(input('Enter a number: '))
z = int(input('Enter a number:'))
print(f'The entered numbers for x, y, and z are {x}, {y}, and {z}, respectively.')
if x>y and x>z:
    print(f'The number x with {x} is the greatest number.')
elif y>x and y>z:
    print(f'The number y with {y} is the greatest number.')
else:
    print(f'The number z with {z} is the greatest number.')


    birth_year = 1990
if birth_year < 1980 or birth_year > 1989:
    print('You were not born in 1980s.')
else:
    print('You were born in 1990s.')
print('Done!')


birth_year = 1990
if not birth_year == 1991:
    print('The year of birth is not 1991.')



    birth_year = int(input('Enter a year of birth: '))
print(f'The entered year of birth is: {birth_year}')
if birth_year < 1985 or birth_year == 1991 or birth_year == 1995:
    print(f'You were born in {birth_year}')
else:
    # For instance, if your year of birth is 1993
    print(f'Your year of birth with {birth_year} is wrong.')


    birth_year = int(input('Enter a year of birth: '))
print(f'The entered year of birth is: {birth_year}')
if birth_year < 1985 or birth_year == 1991 or birth_year == 1995:
    # For instance, if your year of birth is 1995
    print(f'You were born in {birth_year}')
else:
    print(f'Your year of birth with {birth_year} is wrong.')


