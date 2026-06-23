lst1 = [1,2,3]
lst2 = [4,5,6,7]

squared = map(lambda x : x*x, lst1, lst2)   # ! ERROR : when you pass multiple 
print(list(squared))    
# map() stops when the shortest iterable ends.

# Note : writing squared does NOT leads to it's computation, it only happens when squared is called

