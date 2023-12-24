# Employ double quotation marks for describing a string
"Hello World!"


# Employ single quotation marks for describing a string
'Hello World!'

# Digitals and spaces in a string
'3 6 9 2 6 8'


# Specific characters in a string
'@#5_]*$%^&'


# printing a string
print('Hello World!')


# Assigning a string to a variable 'message'
message = 'Hello World!'
print(message)
message


# printing the first element in a string
message = 'Hello World!'
print(message[0])


# Printing the element on index 8 in a string
print(message[8])


# lenght of a string includign spaces
len(message)


# Printing the last element in a string
print(message[11])
# Another comment writing type is as follows using triple quotes.
"""
Although the length of the string is 12, since the indexing in Python starts with 0,
the number of the last element is therefore 11.
"""


# printing the last element of a string
message[-1]


# printing the first element of a string
message[-12]
"""
Since the negative indexing starts with -1, in this case, the negative index number
of the first element is equal to -12.
"""


print(len(message))
len(message)


len('Hello World!')


# Slicing on the variable 'message' with only index 0 to index 5
message[0:5]


# Slicing on the variable 'message' with only index 6 to index 12
message[6:12]


# to select every second element in the variable 'message'
message[::2]


# corporation of slicing and striding
# get every second element in range from index 0 to index 6
message[0:6:2]



message = 'Hello World!'
question = ' How many people are living on the earth?'
statement = message+question
statement


# printing a string for 4 times
4*" Hello World!"



# New line escape sequence
print('Hello World! \nHow many people are living on the earth?')



# Tab escape sequence
print('Hello World! \tHow many people are living on the earth?')


# back slash in a string
print('Hello World! \\ How many people are living on the earth?')
# r will say python that a string will be show as a raw string
print(r'Hello World! \ How many people are living on the earth?')



message = 'hello python!'
print('Before uppercase: ', message )
# convert uppercase the elements in a string
message_upper = message.upper()
print('After uppercase: ', message_upper)
# convert lowercase the elements in a string
message_lower = message.lower()
print('Again lowercase: ', message_lower)
# convert first letter of string to uppercase
message_title = message.title()
print('The first element of the string is uppercase: ', message_title)



# replace() method in a string
message = 'Hello Python!'
message_hi = message.replace('Hello', 'Hi')
message_python = message.replace('Python', 'World')
print(message_hi)
print(message_python)


# find() method application in a string
message = 'Hello World!'
print(message.find('Wo'))
# the output is the index number of the first element of the substring


# find() method application to obtain a substring in a string
message.find('World!')


# if cannot find the substring in a string, the output is -1.
message.find('cndsjnd')


text = 'Jean-Paul Sartre somewhere observed that we each of us make our own hell out of the people around us. Had
# find the first index of the substring 'Nancy'
text.find('Nancy')



# replace the substring 'Nancy' with 'Nancy Lier Cosgrove Mullis'
text.replace('Nancy', 'Nancy Lier Cosgrove Mullis')


# convet the text to lower case
text.lower()


# convert the first letter of the text to capital letter
text.capitalize()


# casefold() method returns a string where all the characters are in lower case
text.casefold()


# center() method will center align the string, using a specified character (space is the default) as the fill character.
message = 'Hallo Leute!'
message.center(50, '-')


# count() method returns the number of elements with the specified value
text.count('and')


# format() method
"""
The format() method formats the specified value(s) and insert them inside the string's placeholder.
The placeholder is defined using curly brackets: {}.
"""
txt = "Hello {word}"
print(txt.format(word = 'World!'))
message1 = 'Hi, My name is {} and I am {} years old.'
print(message1.format('Bob', 36))
message2 = 'Hi, My name is {name} and I am {number} years old.'
print(message2.format(name ='Bob', number = 36))
message3 = 'Hi, My name is {0} and I am {1} years old.'
print(message3.format('Bob', 36))


