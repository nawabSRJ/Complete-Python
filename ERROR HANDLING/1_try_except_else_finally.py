# todo - In this file we are going to implement and understand the else and finally block in try-except

try:
    x = int('123') # no error
except ValueError as e:
    print('Value Error is here :  ', e)

else:
    print('No Value Error Occurred')

finally:
    print('Finally Block ~ When NO Error')


print('\n----Different try-except block now----')

try:
    x = int('abc')

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print('Value Error has occurred : ', e)

else:
    print('Else block on error') # ! didn't run

finally:
    print('Finally Block on error')


# ? Note on finally block : 
# * The finally keyword in Python is used to define a block of code that will be executed no matter what, whether an exception occurs or not. It is often used for cleanup operations, ensuring that certain actions are taken regardless of whether an exception is raised or a return statement is passed
