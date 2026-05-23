"""
============================================
DOCSTRINGS IN PYTHON - MULTI-LINE DOCSTRING
============================================
"""
print(__doc__)

# =========================================================
# MULTI-LINE DOCSTRING
# =========================================================


def add(a, b):
    """
    Add two numbers and return the result.

    Parameters:
        a (int | float): First number
        b (int | float): Second number

    Returns:
        int | float: Sum of a and b
    """

    return a + b


print(add.__doc__)
print('Add 10 and 20 : ',add(10, 20))


# =========================================================
# SINGLE LINE VS MULTI-LINE DOCSTRINGS
# =========================================================


# Good for simple functions

def square(x):
    """Return square of x."""

    return x * x


# Better for detailed explanations

def power(base, exponent):
    """
    Raise a base number to a given exponent.

    Example:
        power(2, 3) -> 8

    Parameters:
        base (int | float): Base value
        exponent (int): Power value

    Returns:
        int | float: Final computed result
    """

    return base ** exponent


print(square(5))
print(power(2, 4))


# =========================================================
# END OF DEMO
# =========================================================

print("\nMulti-line docstring demo completed successfully.")