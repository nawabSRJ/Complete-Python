"""
DOCSTRINGS IN PYTHON
====================

A docstring is a special string used to document:
- Modules
- Functions
- Classes
- Methods

Docstrings are written using triple quotes:
- """  """ 
- '''  '''

Unlike comments:
- Comments explain code to developers
- Docstrings become part of the object itself and can be accessed using help() or __doc__

This folder demonstrates:
1. Module docstrings
2. Function docstrings
3. Class docstrings
4. Method docstrings
5. Accessing docstrings
6. help() function
7. Multi-line docstrings
8. Parameter documentation
9. Return documentation
10. Good practices
"""


# =========================================================
# IMPORTANT DIFFERENCE: COMMENTS VS DOCSTRINGS
# =========================================================


# This is a normal comment.
# Python ignores it at runtime.


def demo():
    """This is a docstring."""

    pass


print(demo.__doc__)


# =========================================================
# END OF DEMO
# =========================================================

print("\nDocstring intro completed successfully.")