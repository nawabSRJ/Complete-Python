# 2_for_loops.py
# Python for loop Notes
# ---------------------
# This file explains how to use for loops in Python.
# It covers syntax, iterating over sequences, using the range() function,
# the "in" keyword, nested loops, loop control statements, and best practices.

# 1. for loop syntax
# ------------------
# A for loop runs once for each item in an iterable.
# The general syntax is:
# for variable in iterable:
#     block_of_code
# The variable receives each item from the iterable one by one.

# Example: iterate over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print("Fruit:", fruit)

# Example: iterate over a string
for char in "Python":
    print(char)

# 2. for loop with the range() function
# -------------------------------------
# range() generates a sequence of integers. It's often used for numeric loops.
# Common forms:
# range(stop)
# range(start, stop)
# range(start, stop, step)

# Example: range(stop)
for i in range(5):
    print("Index:", i)

# Example: range(start, stop)
for i in range(2, 6):
    print("Number:", i)

# Example: range(start, stop, step)
for i in range(0, 10, 2):
    print("Even number:", i)

# 2.1 range() is lazy
# range() does not create a full list in memory. It produces values on demand.
# That makes it efficient for large sequences.

# 3. for loop with "in" and direct iteration
# -------------------------------------------
# The "in" keyword tells Python to loop over items in an iterable.
# You can use it with lists, tuples, strings, dictionaries, sets, and more.

names = ("Sara", "Ali", "Priya")
for name in names:
    print("Hello", name)

# Iterate over dictionary keys
student_scores = {"Amit": 85, "Nita": 92, "Ravi": 78}
for student in student_scores:
    print(student, "=>", student_scores[student])

# Iterate over dictionary items
for student, score in student_scores.items():
    print(student, "scored", score)

# 4. loop control statements
# --------------------------
# - break: stop the loop immediately.
# - continue: skip the rest of the current iteration.
# - else: optional else block runs when the loop finishes normally.

for i in range(6):
    if i == 4:
        print("Stopping at", i)
        break
    print(i)
else:
    print("Loop completed without break")

print("---")

for i in range(6):
    if i % 2 == 0:
        continue    # directly jump to the next iteration
    print("Odd number:", i)
else:
    print("Loop completed normally")

# 5. nested for loops
# -------------------
# A nested loop has one loop inside another.
# Use nested loops when you need to iterate over combinations or 2D data.

for row in range(1, 4):
    for col in range(1, 4):
        print(f"Row {row}, Col {col}")
    print("End of row", row)

# 6. unpacking in for loops
# -------------------------
# You can unpack tuples or lists directly in the for loop header.

pairs = [(1, "one"), (2, "two"), (3, "three")]
for number, word in pairs:
    print(number, "is spelled", word)

print('\nDoing the same with a dictionary:')  # just as we did above
for key,val in student_scores.items():
    print(key, "=>", val)

print('\n')

# 7. useful for loop patterns
# ---------------------------
# - iterate over indexes with range(len(sequence))
# - use enumerate() to get index and value together
# - use zip() to iterate multiple sequences in parallel

colors = ["red", "green", "blue"]
for index in range(len(colors)):
    print(index, colors[index])

for index, color in enumerate(colors, start=1):
    print(index, "=>", color)

numbers = [10, 20, 30]
letters = ["a", "b", "c"]
for num, letter in zip(numbers, letters):
    print(num, letter)

# 8. summary
# ----------
# - for loops iterate over each item in an iterable.
# - range() is useful for numeric sequences and index-based loops.
# - "in" is the keyword used to connect the loop variable to the iterable.
# - break stops the loop, continue skips to the next iteration, and else runs if no break occurs.
# - nested loops, unpacking, enumerate, and zip are common and helpful patterns.
