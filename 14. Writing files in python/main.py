# Writing lines to a file.
fname = 'pcr_file.txt'
with open(fname, 'w') as f:
    f.write("I dedicate this book to Nancy Lier Cosgrove Mullis.\n")
    f.write("Jean-Paul Sartre somewhere observed that we each of us make our own hell out of the people around us. \n")
    f.write("Or maybe he would have just said, 'If I would had a woman like that, my books would not have been about \n")
    f.write("This book is not about despair. It is about a little bit of a lot of things, and, if not a single one of them is wet \n")
    f.write("A feedback from Elle on the book\n")
    f.write("This bona-fide wild card of the scientific community writes with eccentric gusto.… Mullis has created a free \n")





    # Checking the file whether it was written or not
    with open(fname, 'r') as f:
        content = f.read()
    print(content)


    # Writing a list to a file
    added_text = ["From The New Yorker\n",
                  "Entertaini ng … [Mullis is] usefully cranky and combative, raising provocative questions about receive\n",
                  "From Chicago Sun-Times\n",
                  "One of the most unusual scientists of our times, a man who would be a joy to put under a microscope \n",
                  "From Andrew Weil, M.D.\n",
                  "In this entertaining romp through diverse fields of inquiry, [Mullis] displays the openmindedness, ecc\n",
                  ]
    fname = 'sample.txt'
    with open(fname, 'w') as f:
        for line in added_text:
            print(line)
    f.write(line)



    # Wrting and tehn reading the file
    new_file = 'pcr_file.txt'
    with open(new_file, 'w') as f:
        f.write('Overright\n')
    with open(new_file, 'r') as f:
        print(f.read())




    # Writing a new line to the text file
    with open(new_file, 'a') as f: # To append a new line to the text file, use 'a' in the syntax string
        f.write("I dedicate this book to Nancy Lier Cosgrove Mullis.\n")
    f.write("Jean-Paul Sartre somewhere observed that we each of us make our own hell out of the people around us.\n")
    f.write("Or maybe he would have just said, 'If I would had a woman like that, my books would not have been about\n")
    f.write("This book is not about despair. It is about a little bit of a lot of things, and, if not a single one of them is wet\n")
    f.write("A feedback from Elle on the book\n")
    f.write("This bona-fide wild card of the scientific community writes with eccentric gusto.… Mullis has created a free\n")
    # Verification of the new lines in the text file
    with open(new_file, 'r') as f:
        print(f.read())



    fname = 'pcr_file.txt'
    with open(fname, 'a+') as f:
        f.write("From F. Lee Bailey\n")
    f.write("A very good book by a fascinating man.… [Mullis] enjoys an almost frighteningly brilliant mind and yet some\n")
    print(f.read())




    # To verify the text file whether it is added or not
    with open(fname, 'r') as f:
        print(f.read())




    with open(fname, 'a+') as f:
        print("First location: {}".format(f.tell())) # it returns the current position in bytes
    content = f.read()
    if not content:
        print('Read nothing.')
    else:
        print(f.read())

    f.seek(0, 0)
    """
    seek() function is used to change the position of the File Handle to a given specific position.
    File handle is like a cursor, which defines from where the data has to be read or written in the file.
    Syntax: f.seek(offset, from_what), where f is file pointer
    Parameters:
    Offset: Number of positions to move forward
    from_what: It defines point of reference.
    Returns: Return the new absolute position.
    The reference point is selected by the from_what argument. It accepts three values:
    0: sets the reference point at the beginning of the file
    1: sets the reference point at the current file position
    2: sets the reference point at the end of the file
    """
    print('\nSecond location: {}'.format(f.tell()))
    content = f.read()
    if not content:
        print('Read nothing.')
    else:
        print(content)
    print('Location after reading: {}'.format(f.tell()))





    with open(fname, 'r+') as f:
        content=f.readlines()
    f.seek(0,0) # writing at the beginning of the file
    f.write('From The San Diego Union-Tribune' + '\n')
    f.write("Refreshing … brashly confident … indisputably entertaining." + "\n")
    f.write("To my family..." + '\n')
    f.seek(0,0)
    print(f.read())





    # Let's copy the text file 'pcr_file.txt' to another one 'pcr_file_1.txt'
    fname = 'pcr_file.txt'
    with open(fname, 'r') as f_reading:
        with open('pcr_file_1.txt', 'w') as f_writing:
            for line in f_reading:
                f_writing.write(line)




    # For the verification, execute the following codes
    fname = 'pcr_file_1.txt'
    with open(fname, 'r') as f:
        print(f.read())
        # Now, there are 2 files from the same file content.





    # Writing the student names into a file
    fname = open(r'student_name.txt', 'w')
    for i in range(3):
        name = input('Enter a student name: ')
    fname.write(name)
    fname.write('\n') # To write names as a new line
    fname = open(r'student_name.txt', 'r')
    for line in fname:
        print(line)
    fname.close()




    # To write the file
    fname = open(r'student_name.txt', 'w')
    name_list = []
    for i in range(3):
        name = input('Enter a student name: ')
    name_list.append(name + '\n')
    fname.writelines(name_list)
    # To read the file
    fname = open(r'student_name.txt', 'r')
    for line in fname:
        print(line)
    fname.close()




    lines = ['Hello, World!', 'Hi, Python!']
    with open('new_file.txt', 'w') as f:
        for line in lines:
            f.write(line)
            f.write('\n')
    with open('new_file.txt', 'r') as f:
        print(f.read())



    # Add more lines into the file
    more_lines = ['Hi, Sun!', 'Hello, Summer!', 'Hi, See!']
    with open('new_file.txt', 'a') as f:
        f.writelines('\n' .join(more_lines))
    with open('new_file.txt', 'r') as f:
        print(f.read())
    f.close()



