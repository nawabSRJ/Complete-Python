# One of the most interesting things i found is iterating over the content of a file and not really storing it, this is done by using for loop

# normally without indexing lines
def method1():
    with open('sample_text.txt', 'r+') as file:
        print('file object : ',file)
        for line in file:
            print(line)


# with indexing of lines
def method2():
    with open('sample_text.txt', 'r+') as file:
        for index,line in enumerate(file, start=-2):
            print(index, line)

# playing with file pointer
def pointer_play():
    with open('sample_data.txt', 'r+') as file:
        pt1 = file.read()
        print('----All the content : ----\n', pt1, end='\n\n')
        pt2 = file.read(5)
        print('----Next 5 : ', pt2)
        # you will not get anything here because there is nothing after the end of the file, since the read() function has read all the content and is currently at the end of the file
        # ! So can we bring back the file pointer to our desired location?
        # ? Yes, using .seek() method
        file.seek(0)    # pass index of the desired location
        pt3=file.read(5)
        print('Using pt2 : ',pt2) # once again
        print('Using pt3 : ',pt3)




