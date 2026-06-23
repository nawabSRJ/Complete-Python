# todo : imagine you have a list of numbers and then you have to remove null or empty values from it

print(bool(None) == False)  # so basically the boolean equivalent of None is False

users = ['Srajan', 'Aditya', 'Raman', '', None,'None', '  ']

filtered_users = filter(lambda x:bool(x),users)
filtered_users = filter(bool,users)
# both the above give the same results
print(list(filtered_users))

# ! NOTE : whitespace characters are True in python


# todo : to remove falsy values

values = [0, 1, "", "Hello", None, [], [1,2], False, True]

print(list(filter(None, values)))
print(list(filter(lambda x:bool(x), values)))
print(list(filter(lambda x:bool(x), values)))

# All 3 give the same results, None can be used to remove falsy values

# * IMPORTANT : unlike map(), filter accepts only one iterable  
