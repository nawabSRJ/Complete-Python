"""
DOCSTRINGS IN PYTHON - BEST PRACTICES & PEP 257
================================================
"""


# =========================================================
# DOCSTRING BEST PRACTICES
# =========================================================

"""
BEST PRACTICES:

1. Write docstrings for:
   - Public functions
   - Classes
   - Modules
   - Important methods

2. Start with a short summary line.

3. Use clear and concise language.

4. Explain:
   - Parameters
   - Return values
   - Exceptions raised

5. Keep docstrings updated.

6. Follow PEP 257 conventions.
"""


# =========================================================
# PEP 257 STYLE EXAMPLE
# =========================================================


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): Length of rectangle.
        width (float): Width of rectangle.

    Returns:
        float: Area of rectangle.
    """

    return length * width


print(calculate_area(5, 3))


# =========================================================
# END OF DEMO
# =========================================================

print("\nBest practices & PEP 257 demo completed successfully.")