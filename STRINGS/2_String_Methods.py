base = "  Hello-World  \n"

# search and membership
print(base.find("lo"))         # 3
print(base.rfind("lo"))        # 10
print(base.index("Hello"))      # 2
print("World" in base)         # True
print(base.count("l"))         # number of occurrences

# find/index difference: index raises, find returns -1
print(base.find("missing"))
try:
    print(base.index("missing"))
except ValueError as exc:
    print("ValueError:", exc)

# split and partition semantics
print(base.split())             # whitespace split
print(base.split("-"))         # split on hyphen
print(base.rsplit("-", 1))
print(base.splitlines())
print(base.partition("-"))      # always 3-tuple
print(base.rpartition("-"))
print(base.partition("missing"))

# strip and character sets are not substrings
print(repr(base.strip()))        # removes whitespace on both sides
print(repr(base.strip(" Hld\n")))
print(repr(base.lstrip()))
print(repr(base.rstrip()))

# case conversions and comparisons
sample = "Straße"
print(sample.lower())
print(sample.upper())
print(sample.casefold())         # stronger normalization for comparisons
print("ß".casefold())
print("Hello".swapcase())
print("hello".capitalize())
print("hello world".title())

# type-like queries on empty strings vs content
print("".islower(), "".isupper(), "".isalpha())
print("abc".isalpha(), "abc123".isalnum(), "123".isnumeric())
print(" ".isspace(), "abc".isascii())

# join requires all items to be strings
joined = ",".join(["a", "b", "c"])
print(joined)
# print(" ".join(["a", 1, "c"]))  # TypeError if uncommented

# replacement rules
print("banana".replace("a", "o", 2))   # bonana
print("banana".replace("x", "y"))      # unchanged if missing
print("abc".replace("", "-") )         # inserts between characters

# translate and maketrans for multiple replacements at once
mapping = str.maketrans({"H": "h", "e": "E", "-": None})
print("Hello-World".translate(mapping))

# padding and alignment
print("42".zfill(5))
print("hi".rjust(5, "."))
print("hi".ljust(5, "_"))
print("hi".center(5, "*"))

# format_map and f-string differences
d = {"name": "Alice", "age": 30}
print("{name} is {age}".format_map(d))
print(f"{d['name']} is {d['age']}")

# split with None behaves differently from explicit whitespace separator
print("  one   two  ".split())    # ['one', 'two']
print("  one   two  ".split(" ")) # retains empty segments

# splitlines preserves line breaks with keepends=True
print("a\nb\r\nc".splitlines(True))

# isidentifier is useful for validating variable names
print("var_name".isidentifier(), "123abc".isidentifier())

# bytes-only operations: encode returns bytes, not a string
encoded = "hello".encode("utf-8")
print(encoded, type(encoded))

# most string methods return a new string because strings are immutable
original = "abc"
modified = original.replace("a", "z")
print(original, modified)
