# 3_while_loops.py
# Python while loop Notes
# -----------------------
# This file explains how to use while loops in Python.
# It covers syntax, loop conditions, loop control, using while with input,
# and best practices for writing safe and readable loops.

# 1. while loop syntax
# --------------------
# A while loop repeats as long as a condition remains True.
# The general syntax is:
# while condition:
#     block_of_code
# The condition is evaluated before each iteration.

# Example: simple while loop
count = 1
while count <= 5:
    print("Count:", count)
    count += 1

# 2. while loops with boolean conditions
# --------------------------------------
# The loop continues until the condition becomes False.
# You must update values used in the condition inside the loop.

balance = 10
while balance > 0:
    print("Balance remains", balance)
    balance -= 3
print("Balance is zero or negative, exiting loop")

# 3. while loop with user input
# -----------------------------
# while is often used when input or external data determines when to stop.
# Example: prompt the user until they provide valid input.
while True:
    answer = input("Type yes to continue or no to stop: ").strip().lower()
    if answer == "yes":
        print("Continuing...")
        break
    elif answer == "no":
        print("Stopping...")
        break
    else:
        print("Please type yes or no.")

print('\n')
# 4. sentinel-controlled loops
# ---------------------------
# A sentinel value signals the end of input. Use while with a special value.

value = input("Enter a number or 'done' to finish: ")
while value.lower() != "done":
    number = float(value)
    print("You entered", number)
    value = input("Enter a number or 'done' to finish: ")
print("Finished reading values")

print('\n')
# 5. loop control statements in while loops
# ----------------------------------------
# - break stops the loop immediately.
# - continue skips the current iteration and checks the condition again.
# - else runs when the loop exits without break.

i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Skipping", i)
        continue
    print("Value:", i)
else:
    print("While loop finished normally")

print('\n')
# 6. infinite loops and safe exit
# -------------------------------
# A while True loop runs forever unless break is used.
# Always include a clear exit condition to avoid unintentional infinite loops.

while True:
    word = input("Enter a word or press Enter to quit: ")
    if word == "":
        print("Exiting loop")
        break
    print("You typed:", word)

# 7. while loops with else
# ------------------------
# The else block executes when the loop condition becomes False naturally.
# It does not run if the loop is exited by break.

n = 1
while n < 3:
    print("n is", n)
    n += 1
else:
    print("Loop ended because condition became false")

print('\n')
# 8. comparing for and while loops
# --------------------------------
# - for loops are best for iterating over a known sequence.
# - while loops are best when the number of iterations depends on a condition.
# - Both loops can use break and continue.
# - Use while when input, external conditions, or sentinel values control loop exit.

print('\n')
# 9. summary
# ----------
# - while loops repeat while a condition stays True.
# - ensure the condition changes inside the loop to avoid infinite loops.
# - use break to stop when a desired condition occurs.
# - while is ideal for user input, sentinel values, and condition-driven repetition.
