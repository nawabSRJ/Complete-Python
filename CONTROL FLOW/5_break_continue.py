# More detailed examples on break and continue
# In python these can only be used in loops

# 'break' is NOT used in match-case unlike C++ or JS where break is used in switch case conditional programming

# * One place where we use it definitely is the While True loop conditions where we need to recursively take the user input and only break under certain conditions

while True:
    ask = int(input('Enter an even number : '))
    if ask % 2==0:
        print('Even number entered\nExiting loop....')
        break
    else:
        print('Please enter an even number only to exit')


# ? 'continue' is used when we want to skip the current iteration and move to the next one

print('\nPrinting odd numbers from 1 to 10 using continue statement')
for i in range(1,11):
    if i % 2 == 0:
        continue # skip the even numbers
    print(i) # only odd numbers will be printed