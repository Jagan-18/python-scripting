# Reading the txt file
file_name = "pcr_file.txt"
file = open(file_name, "r")
content = file.read()
content



# Printing the path of file
print(file.name)
# Printing the mode of file
print(file.mode)
# Printing the file with '\n' as a new file
print(content)
# Printing the type of file
print(type(content))



# Close the file
file.close()



# Verification of the closed file
file.closed



# See the content of the file
print(content)



# Reading the first 20 characters in the text file
with open(fname, 'r') as f:
    print(f.read(20))



    # Reading certain amount of characters in the file
with open(fname, 'r') as f:
    print(f.read(20))
    print(f.read(20))
    print(f.read(50))
    print(f.read(100))



    # Reading first line in the text file
with open(fname, 'r') as f:
    print('The first line is: ', f.readline())



# Difference between read() and readline()
with open(fname, 'r') as f:
    print(f.readline(20))
    print(f.read(20)) # This code returns the next 20 characters in the line.




with open(fname, 'r') as f:
    line_number = 1
    for line in f:
        print('Line number', str(line_number), ':', line)
    line_number+=1



with open(fname, 'r') as f:
    print(f.read())



with open(fname, 'r') as f:
    print(f.read(30))



with open(fname, 'r') as f:
    file_list = f.readlines()
    # Printing the first line
    print(file_list[0])
    # Printing the second line
    print(file_list[1])
    # Printing the third line
    print(file_list[2])
    # Printing the fourth line
    print(file_list[3])



fname = r'C:/Users/test/Desktop/PROGRAMMING_WEB DEVELOPMENT/PYTHON_TUTORIAL/01. python_files_for_sha'
with open(fname, 'r') as f:
    content=f.readlines()
    print(content)



with open(fname, 'r') as f:
    len_file = 0
    total_len_file = 0
    for line in f:
    # Total length of line in the text file
        total_len_file = total_len_file+len(line)
    # Lenght of the line after removing leading and trailing spaces
    len_file = len_file+len(line.strip())
    print(f'Total lenght of the line is {total_len_file}.')
    print(f'The length of the line after removing leading and trailing spaces is {len_file}.')


with open(fname, 'r') as f:
    str = ""
    for line in f:
        str+=line
    print(f'The size of the text file is {len(str)}.')




with open(fname, 'r') as f:
    count = 0
    for line in f:
        count = count + 1
    print(f'The number of lines in the text file is {count}.')




