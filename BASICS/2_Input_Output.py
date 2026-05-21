# 2_Input_Output.py
# Python Input and Output (I/O) Notes
# -----------------------------------
# This file demonstrates how to read input from the user and print output.
# It also explains the default behavior, how data types are handled, and
# how to convert values when needed.

# 1. Output using print()
# ----------------------
# The print() function sends text to the console. It can display multiple values,
# add separators, and control line endings.

name = "Srajan"
age = 21
is_student = True

print("Name:", name)
print("Age:", age)
print("Is student:", is_student)

# The default separator between print() arguments is a single space.
# The default end character is a newline ("\n"), so print() moves to the next line.
print("Hello", "world")
print("This is the first line.", end=" ")
print("This is still the same line.")

# Custom separators and line endings:
print("A", "B", "C", sep="-")
print("One line", end="***")
print("Another line")

# 2. Input using input()
# ----------------------
# input() reads a line from the user and always returns a string.
# If the user types 123 and presses Enter, the returned value is "123", not 123.

# prompt_text is shown to the user before waiting for input.
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello", first_name, last_name)

# 2.1 Default input data type
# The default type of any value returned by input() is str.
user_value = input("Enter anything: ")
print("You entered:", user_value, "of type", type(user_value))

# 3. Converting input values to other types
# -----------------------------------------
# Most real programs need numeric values, so we often convert the input string.
# If the input cannot be converted, Python raises a ValueError.

tag = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
likes_python = input("Do you like Python? (yes/no): ").strip().lower() == "yes"

print("Type of age:", type(tag), "value:", tag)
print("Type of height:", type(height), "value:", height)
print("Likes Python:", likes_python, type(likes_python))

# 3.1 Why conversion is needed
# The input() function returns a string, so arithmetic operations require a cast.
# Without conversion, values like "10" + "5" produce string concatenation.

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
print("Without conversion, strings concatenate:", num1 + num2)

num1_int = int(num1)
num2_int = int(num2)
print("After converting to int, addition works:", num1_int + num2_int)

# 3.2 Converting to different Python data types
# int(): integer
# float(): floating point number
# str(): string
# bool(): boolean conversion follows Python truthiness rules
# Note: bool("False") is True because non-empty strings are truthy.

value = "0"
print("bool('0') =>", bool(value))
value = ""
print("bool('') =>", bool(value))

# 4. Handling invalid conversions
# --------------------------------
# Use try/except to avoid crashes if the user enters invalid data.

while True:
    raw = input("Enter an integer value: ")
    try:
        valid_int = int(raw)
        print("You entered the integer", valid_int)
        break
    except ValueError:
        print("That is not a valid integer. Please try again.")

# 5. Formatting output
# --------------------
# f-strings are the modern, readable way to interpolate values into strings.

temperature = 25.5
print(f"Current temperature: {temperature} °C")
print(f"Name: {first_name} {last_name}, Age: {tag}")

# 5.1 Formatting numbers
print(f"Height with 2 decimals: {height:.2f}")

# 6. Input and changing data types
# --------------------------------
# You can use input() and immediately convert the value in one expression.
# This is useful when the input must have a specific type.

score = float(input("Enter your test score: "))
print(type(score), score)

# 6.1 Complex conversions
# If you need a list of numbers, split the string and convert each item.
line = input("Enter three values separated by spaces: ")
parts = line.split()
print("Raw parts:", parts)

if len(parts) >= 3:
    a = int(parts[0])
    b = float(parts[1])
    c = parts[2]  # leave as string
    print("Converted values:", a, b, c)
else:
    print("Not enough values provided.")

# 7. Useful I/O details and defaults
# ----------------------------------
# - input() always returns a string.
# - print() converts non-string values to strings automatically.
# - The default print separator is a space, and the default end is a newline.
# - If you want an empty input value, pressing Enter returns an empty string "".
# - When reading numbers, always convert to int/float before doing math.
# - For boolean questions, normalize input with strip() and lower().

empty_input = input("Press Enter without typing anything: ")
print("Empty input value:" , repr(empty_input), "length:", len(empty_input))

# 8. Input with default values in code
# ------------------------------------
# You can provide a fallback default after reading raw input.
raw_age = input("Enter your age (or press Enter to use 18): ")
age_with_default = int(raw_age) if raw_age != "" else 18
print("Age with default:", age_with_default)

# 9. Summary comments
# -------------------
# Use input() to ask the user for values.
# Use print() to show values.
# Remember: input() returns str, so convert to int/float/bool as needed.
# Handle conversion errors with try/except for robust programs.
# Use f-strings, sep, and end to make output clean and readable.
