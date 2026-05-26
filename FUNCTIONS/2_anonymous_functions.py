# Anonymous functions are functions that do not have a name.
# In Python, the only anonymous function syntax is the lambda expression.
# They are useful when you need a short, throwaway function for a small task,
# especially when passing a function as an argument.

# A normal named function:

def square(x):
    return x * x

print(square(5))  # 25

# An anonymous function using lambda:

anonymous_square = lambda x: x * x
print(anonymous_square(5))  # 25

# Why use anonymous functions?
# - The function body is simple and short.
# - You do not need to reuse the function elsewhere.
# - It keeps code concise when used inside a larger expression.

# Practical example: use lambda when you want a small function passed directly
# to another function, such as sorting or filtering data.

numbers = [3, 1, 4, 2]
print(sorted(numbers, key=lambda x: -x))  # [4, 3, 2, 1]

# Note: Anonymous functions are not a replacement for normal functions.
# Use named functions when the logic is more than one expression or when clarity is more important.
