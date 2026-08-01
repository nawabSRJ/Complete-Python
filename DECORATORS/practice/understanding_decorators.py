# We know what decorators are, but how do they work exactly, that is what we will see in this file

def decorator(func):

    def wrapper():
        print("Before")
        func()
        print("After")
        


    return wrapper  # Not wrapper(), we are not calling here, only pass the reference to the wrapper function object

    # received func from args, but returned wrapper, and wrapper is the function that will call the received function "func" 

# * we have to define the decorator function first
@decorator
def greet():
    print("Greetings!!")

greet()