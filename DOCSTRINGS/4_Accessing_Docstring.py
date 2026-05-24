"""
DOCSTRINGS IN PYTHON - ACCESSING DOCSTRINGS
============================================
"""


def greet(name):
    """Return a greeting message for the given name."""

    return f"Hello, {name}!"


def square(x):
    """Return square of x."""

    return x * x


class Student:
    """
    Represents a student object.

    Attributes:
        name (str): Name of the student
        age (int): Age of the student
    """

    def __init__(self, name, age):
        """Initialize the student object."""

        self.name = name
        self.age = age

    def introduce(self):
        """Return an introduction message."""

        return f"My name is {self.name} and I am {self.age} years old."


# =========================================================
# ACCESSING DOCSTRINGS DIRECTLY
# =========================================================


print("\n--- Accessing Docstrings ---")

print(greet.__doc__)
print(square.__doc__)
print(Student.__doc__)


# =========================================================
# USING help()
# =========================================================

# Uncomment these lines to see detailed documentation output
print('From help() function:')
help(greet)
help(square)
help(Student)


# =========================================================
# END OF DEMO
# =========================================================

print("\nAccessing docstrings demo completed successfully.")