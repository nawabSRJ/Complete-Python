def process_pair(x, *y,z):
    # return f"x={x}, y={y}, sum={x+y}"
    return f'x={x}, rest = {y}, z={z}'

result = process_pair(5, 10,15,z=20)
print("Direct call process_pair(5, 10):", result)

print('Sequence Unpacking on list : ')
x,*y,z = [1,2,3,4]
print(x)
print(y)
print(z)

print('Sequence Unpacking on tuple : ')
x,*y,z = (1,2,3,4)
print(x)
print(y)
print(z)


def show_cords(x,y,z):
    return f'x={x}, y={y}, z={z}'

point = (1,2,10)
print(show_cords(*point))
# print(show_cords(point))  # ! ERROR : Because this is just a single argument and the show_cords function expects 3, thus, when using the asterick operator to unpack the total no. of args becomes 3 
point2 = (1,2,3,4)
# print(show_cords(*point2))  # ! ERROR, takes 3 positional arguments but 4 were given

