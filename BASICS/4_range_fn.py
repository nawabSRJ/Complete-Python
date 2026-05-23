print(range(4)) # weird output

print(list(range(4)))

print(tuple(range(4)))
# print(dict(range(4))) # ! ERROR

for i in range(4):
    print(f'This is i : {i}', end=' | ')

# ? Syntax is:
# ? range(stop) : when one arg passed
# ? range(start,stop) : when two args passed
# ? range(start,stop,step) : when three args passed, NEVER goes to or beyond stop



