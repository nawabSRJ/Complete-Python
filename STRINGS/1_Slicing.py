# start:end, it is inclusive of start, exclusive of end
text = "interview"
print(text[0:3])   # int
print(text[3:])    # erview -> [start:] means from start to end OR by default end is len(text)
print(text[:3])    # int    -> [:end] means from 0th index to end OR by default start is 0
print(text[:])     # interview [0:len(text)] is the whole string

# * In the 2nd example you will see the end as len(text) because it is exclusive and the last valid index is len(text)-1. So len(text) essentially means the slicing will happen till the end of the string or the last valid index which is 1 less than len(text).

# omitted start/end are normalized; no IndexError for out-of-bounds bounds
print('\nNo out of bounds error : ',text[-100:100])  # interview
print('Empty string : ',text[100:200])   # empty string

print('\n----Step introduction----\n')
# step controls the stride; step=0 is invalid
print('Step 2:',text[::2])   # every second character
print('Step 2 (starting from index 1):',text[1::2])  # odd positions
try:
    print(text[::0])
except ValueError as exc:
    print("\nValueError:", exc)

# reversing with negative step is a common trick
print('Reversed:',text[::-1])   # weivretni
print('Reversed (up to index 1):',text[5:1:-1]) # erview reversed up to but not including index 1

# negative step changes how start and end are interpreted
print('Step -1 (7:3):',text[7:3:-1]) # evir
print('Step -1 (7:3):',text[7:3])    # empty because step is positive by default

# empty slices vs valid slices
print('Empty slice [2:2]:',text[2:2])   # empty
print('Empty slice [5:3]:',text[5:3])   # empty
print('Empty slice [5:3:-1]:',text[5:3:-1])

# slice objects make the semantics explicit and are useful in generic code
sl = slice(None, None, -1)
print('Sliced with slice object:',text[sl])
print('Indices for slice object:',sl.indices(len(text)))

# slicing a string always returns a string; the original is unchanged
slice_copy = text[:]
print('Slice copy is original:',slice_copy is text)
print('Slice copy equals original:',slice_copy == text)

# a single-character slice is still a string of length 1
print('Single character slice:',text[2:3], len(text[2:3]))

# combining slicing with indexing works, often seen in tricky expressions
print('Combined slicing and indexing:',text[1:5][2])   # same as text[3]
