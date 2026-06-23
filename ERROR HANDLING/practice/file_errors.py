# todo : try to open a file non existent and handle the errors

try:
    with open('mynewfile.txt','r') as file:
        print(file.read())
    
except FileNotFoundError as e:
    print(e)
finally:
    print('Control is here')
    