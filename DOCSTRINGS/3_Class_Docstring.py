"""
=======================================
DOCSTRINGS IN PYTHON - CLASS DOCSTRING
=======================================
"""


# =========================================================
# CLASS DOCSTRING
# =========================================================


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


student1 = Student("Srajan", 20)

print(student1.introduce())
print(Student.__doc__)
print(Student.introduce.__doc__)


# =========================================================
# END OF DEMO
# =========================================================

print("\nClass docstring demo completed successfully.")