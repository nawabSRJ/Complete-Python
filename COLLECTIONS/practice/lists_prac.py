lst = [1,2,3]
lst.reverse()
print(lst)

lst.sort()
print(lst)

lst.sort(reverse=True)
print(lst)

lst.insert(-1,4)    # good tricky thing
print(lst)

lst.append(5)
print(lst)

lstnew = [1,2,3]
print(f'{lstnew}' * 4)

lst = [10,11,12]
tup = (13,14,15)
lst.extend(tup)
print(lst)
print('index of 14 in lst : ', lst.index(14))
print(sorted(lst))
print(lst.sort())   # Returns None because .sort() sorts in place and doesn't return anything

print(lst.reverse())    # Returns None because of the same above reason ~ works in place

print([1,2,3]+[4,5,6])
print((1,2,3)+(4,5,6))