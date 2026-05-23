# string indexing returns a one-character string, not a separate char type
s = "python"
print(s[0], s[-1])  # p n
print(type(s[0]))    # <class 'str'>

# negative indices count backward from the end; -len(s) is the first element
print('Negative Indices:', s[-len(s)], s[-2])

# -0 is identical to 0, which can be a subtle gotcha in expressions
print(s[-0], s[0])

# if the index is out of range, Python raises IndexError immediately
try:
    print(s[10])
except IndexError as exc:
    print("IndexError:", exc)

# dynamic indexing is common in interview questions
first = s[0]
last = s[len(s) - 1]
print(f'First: {first}, Last: {last}')

# strings are immutable, so assignment by index is not allowed
# s[0] = "P"  # TypeError: 'str' object does not support item assignment

# indexing is a single position access; slicing is separate and can return a substring
single = s[1]
one_char_substring = s[1:2]
print(single, one_char_substring, len(single), len(one_char_substring))

# empty strings have no valid index positions
empty = ""
try:
    empty[0]
except IndexError as exc:
    print("empty index error:", exc)
