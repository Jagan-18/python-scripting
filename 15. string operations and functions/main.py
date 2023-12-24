string_hello = 'Hello'
string_python = 'Python!'
print(string_hello)
print(string_python)



text = 'Python is a programming language.'
print(text)
del text[1]
print(text)



text = 'Python is a programming language.'
print(text)
del text
print(text)


text1 = 'Hello '
text2 = 'Python!'
new_text = text1 + text2
print(new_text)



text1 = 'Hello '
text2 = 'Python!'
text1+=text2
print(text1)


text = 'Hello, Python! '
print(text*4)



text = 'Hello, Python!'
print(text[0:5]) # Pozitive indexing
print(text[4])
print(text[-7:]) # Negative indexing
print(text[-7:-1])


text = 'Hello, Python!'
print(len(text))
print(text[:14]) # Default stride value is 1.
print(text[0:14:2])
print(text[::3])




text = 'Hello, Python!'
print(text[::-1])


text = 'Hello, Python!'
print('H' in text)
print('H' not in text)
print('c' not in text)
print('c' in text)



text = 'hello, python!'
print(f'Before capitalizing: {text}')
text = text.capitalize()
print(f'After capitalizing: {text}')




text = 'Hello, Python!'
print(f'Before casefold: {text}')
text = text.casefold()
print(f'After casefold: {text}')



text = 'Hello, Python!'
print(f'Before center() function: {text}')
text = text.center(50)
print(f'After center() function: {text}')
new_text = 'Hi, Python!'
new_text = new_text.center(50, '-')
print(f'After center() function: {new_text}')


text = 'Hello, Python!'
print(f"The number of the character 'o' in the string is {text.count('o')}.")


text = 'Hello, Python!'
text = text.endswith('Python!')
print(text)
new_text = 'Hi, Python!'
new_text = new_text.endswith('World!')
print(new_text)




text = 'Hello, Python!'
print(text.find('Python'))
print(text.find('World', 0, 14)) # It returns -1 if the value is not found.



text = 'Hello {} and Hi {}'.format('World!', 'Python!')
print(text)
text = 'Hello {world} and Hi {python}'.format(world='World!', python='Python!')
print(text)
text = 'Hello {0} and Hi {1}'.format('World!', 'Python!')
print(text)
text = 'Hello {1} and Hi {0}'.format('World!', 'Python!')
print(text)


text = 'Hello, Python!'
print(text.index('Python!'))
print(text.index('Hello'))
print(text.index('Hi')) # If the value is not found, it returns a 'ValueError'




text = 'Hello, Python!'
print(text.isalnum())
msg = 'Hello1358'
print(msg.isalnum())


text = 'Hello'
print(text.isalpha())
text = 'Hello1358' # The text contains numbers.
print(text.isalpha())
text = 'Hello Python!' # The text contains a white space.
print(text.isalpha())


text = 'Hello'
print(text.isdecimal())
numbered_text = '011235813'
print(numbered_text.isdecimal())



numbered_text = '011235813'
print(numbered_text.isdigit())


numbered_text = '011235813'
print(numbered_text.isidentifier())
variable = 'numbered_text'
print(variable.isidentifier())


text = 'Hello, Python!'
print(text.isprintable())
new_text = 'Hello, \n Python!'
print(new_text.isprintable())
space = ' '
print(space.isprintable())



text = 'Hello, Python!'
print(text.isspace())
space = ' '
print(space.isspace())




text = 'Hello, Python!'
print(text.islower())
text = text.lower() # It converts to lower case all the characters in the string.
print(text.islower()) # Now, it returns True.



text = 'Hello, Python!'
print(text.isupper())
text = text.upper() # It converts to upper case all the characters in the string.
print(text.isupper()) # Now, it returns True.


text_list = ['Hello', 'World', 'Hi', 'Python']
print('#'. join(text_list))
text_tuple = ('Hello', 'World', 'Hi', 'Python')
print('+'. join(text_tuple))
text_set = {'Hello', 'World', 'Hi', 'Python'}
print('--'. join(text_set))
text_dict = {'val1': 'Hello', 'val2': 'World', 'val3': 'Hi', 'val4': 'Python'}
print('--'. join(text_dict))


text = 'Python'
text = text.ljust(30, '-')
print(text, 'is my favorite programming language.')



text = 'Python'
text = text.rjust(30, '-')
print(text, 'is my favorite programming language.')


text = ' Hello Python! '
print(text.lstrip()) # It did not delete the white spaces in the right side.


text = ' Hello Python! '
print(text.rstrip()) # It did not delete the white spaces in the left side.




text = ' Hello Python! '
print(text.strip()) # It deleted the white spaces in the both side.


text = 'JavaScript is a programming language.'
print(text)
modified_text = text.replace('JavaScript', 'Python', 1)
print(modified_text)


text = 'Jython is a programming language.'
print(text)
modified_text = text.replace('J', 'P')
print(modified_text)


text = 'Hello World!, Hi Python!'
print(text.partition('Hi'))


text = 'Hello, Python is my favorite programming language.'
print(f"'Python' is in the position {text.rfind('Python')}.")
print(f"'my' is in the position {text.rfind('my')}.")
print(f"'close' is in the position {text.rfind('close')}.")



text = 'Hello, Python is my favorite programming language.'
print(f"'Python' is in the position {text.rindex('Python')}.")
print(f"'my' is in the position {text.rindex('my')}.")
print(f"'close' is in the position {text.rindex('close')}.")


text = 'Hello Python!'
print(text.swapcase())
text = 'hELLO pYTHON!'
print(text.swapcase())




text = 'hello world, hi python!'
print(text.title())

