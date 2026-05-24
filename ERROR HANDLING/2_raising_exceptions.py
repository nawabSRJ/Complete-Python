# Raising Exceptions in Python
# In Python, you can raise exceptions explicitly when your code detects an invalid condition or when you want to stop execution deliberately.

# ! Syntax for raising an exception
# raise <ExceptionType>(<optional message>)
# Example:
# raise ValueError('Value must be positive')

# 1) Raising a built-in exception with a message
x = -5
if x < 0:
    raise ValueError('x must be non-negative')

# 2) Using raise without arguments inside an except block
#    This re-raises the current exception and preserves the original traceback.
try:
    n = int('abc')
except ValueError:
    print('Caught a ValueError, now re-raising')
    raise

# 3) Raising the same exception object again (chaining)
try:
    raise KeyError('Missing key')
except KeyError as err:
    raise KeyError('Wrapped key error') from err

# 4) Using assert for sanity checks
#    assert <condition>, <message>
#    This raises AssertionError if the condition is False.
#    Note: assert statements can be disabled with Python optimization (-O), so do not use asserts for critical runtime checks.
value = 10
assert value > 0, 'Value must be positive'

# 5) Common built-in exception types to raise
#    ValueError   - invalid value or type for an operation
#    TypeError    - wrong type passed to a function
#    IndexError   - invalid index access
#    KeyError     - missing dictionary key
#    RuntimeError - generic runtime issue
#    IOError      - input/output failure
#    FileNotFoundError - missing file access

# 6) Raising exceptions from helper functions
#    Keep logic clear: if a function cannot complete normally, raise an exception.

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError('Denominator cannot be zero')
    return a / b

try:
    print(divide(10, 0))
except ZeroDivisionError as err:
    print('Handled error:', err)

# 7) Best practices when raising exceptions
# - Use a specific exception type rather than the generic Exception.
# - Provide informative error messages.
# - Avoid using bare raise outside exception handling unless re-raising the current exception.
# - Prefer raising built-in exceptions when appropriate.

# 8) Raising a custom exception type (brief preview)
#    Custom exceptions are useful when you want a domain-specific error class.
class InvalidAgeError(ValueError):
    pass

age = -1
if age < 0:
    raise InvalidAgeError('Age cannot be negative')
