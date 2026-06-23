def write_method():
    print("1. Using write() method:")
    with open('output1.txt', 'w') as file:
        file.write("Hello, World!\n")
        file.write(" Welcome to file handling.")
        file.write("This is on the same line.")

    # Read back the file to verify
    with open('output1.txt', 'r') as file:
        print("File content:", repr(file.read()))


def x_method():
    print('Create file method : ')
    with open('myfile.txt', 'x') as file:
        file.write('Hey there, in x mode') # writes to file
        content = file.read()
        print('Read in x mode : ',content)  # ! ERROR ~ Unsupported Method
    ''' You can write but not read in x mode'''

x_method()