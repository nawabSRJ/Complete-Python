# ? Also called "Exception Handling" 
# * In Python, try-except is a mechanism for handling exceptions or errors in a program. The try block contains the code that might raise an exception, and the except block contains the code that handles the exception if it occurs.

# ! What is an exception?
# ? When Python hits something it cannot handle during execution — dividing by zero, opening a missing file, indexing out of range — it stops and raises an exception: a signal that something went wrong. If you don't catch it, the program crashes with a traceback.

# ! Exception vs Syntax Error
# ? A SyntaxError happens before the program runs (bad code). An Exception happens at runtime (valid code, unexpected situation).

# ! Full block structure of try-except-else-finally
# try
# → code that might raise error
# except (if error)
# → handle if error raised
# else (if no error)
# → runs only on success or no error in try block
# finally (always)
# → always runs no matter error occurred or not

# todo - explore basic try-except
# Bare except catches everything including KeyboardInterrupt and SystemExit. Avoid in production — always name the exception type.

try:
    num = int(input('Enter a number >0 : '))
    print(num/0)

except:
    print('Some Error\nWhat error? That is unknown?\n')
    # if the above statement prints that means ~ Error Occurred


# todo - more detail with bare try-except
# ? Now we are going to use Exception class, which is the base class for all the exceptions in python or in other wors, all the exceptions inherit from this class
print('Using Exception base class : ')
try:
    num = int(input('Enter a number >0 : '))
    print(num/0)

except Exception as e:
    print('Some Error : ', e)
    # Now here you will get zero division error mentioned


# todo - handling specific exceptions
print('\nCatching Specific exception : ')
try:
    x = int('abc')
# except ValueError:                    # * NO ISSUE, you can also write like this
#     print('Value Error Occurred')     # * But, here to get details we used below method

except ValueError as e:
    print('Value Error : ', e)



# ! If the error checked and the error raised is different then what?
try:
    print('Making Value Error!')
    x = int('abc')
except ZeroDivisionError:
    print('Zero Division Error Occurred')

except:
    print('\n----Multiple except block allowed----\nSo if this was not there then the program would have crashed')



# ! Why are multiple except block allowed?
# ? Because in the same try block there can be multiple specific exceptions that can be raised or can occur



