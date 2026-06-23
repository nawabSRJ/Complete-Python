# writing a function to demonstrate type of arguments

def name(fname , lname = "Saxena"):  # *default Arguments
    print("Hello",fname,lname)

name("Srajan")
name("Stuti")
name("Shivam")

name("Arush","Tiwari")  # * default arg. will be overriden by function calling arg

# !------------------------------------------------------------------------------

# * taking tuple as function arguments and unpacking it inside the funciton using asterisk(*) operator

def average(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is = ",sum/ len(numbers))

average(5,5)
average(5,5,2)

# ! Tip : generally there is a convention of naming in *args
# so, this is like : 

def student_list(*args):
    for index,name in enumerate(args):
        print(f'{index} : {name}')
    print('All students printed')

student_list('Srajan', 'Adi', 'Pratham', 'Vaibhav')
student_list(['Srajan', 'Adi', 'Pratham', 'Vaibhav'])   # Notice the tricky thing here, this is one single argument and not multiple arguments, the *args used to unpack the arguments not a list of arguments of tuple or basically collections.
