# We know what decorators are, but how do they work exactly, that is what we will see in this file

def decorator(func):

    def wrapper(*args):
        print("Before")
        func(*args)
        print("After")
        


    return wrapper  # Not wrapper(), we are not calling here, only pass the reference to the wrapper function object

    # received func from args, but returned wrapper, and wrapper is the function that will call the received function "func" 

# * we have to define the decorator function first
@decorator
def greet(param, param2):
    print("Greetings!!", param, " and ", param2)

greet("Srajan", "Pratham") # now since the decorator has been applied on this function, so internally this line is "decorator(greet)", and inside of this when wrapper is returned that is calling the actual greet function

# ? Note : As a convention, the wrapper functions use *args, **kwargs 
# because the function on which decorator is applied can have any no. of args, so it is better to use *args technique

