# ? NOTE : python does NOT need a 'break' statement in match-case unlike the C++ switch case because here the control doesn't fall through and execution stops after matched case.


choice = int(input('Enter a no. of your choice between 1-5: '))
match choice:
    case 1:
        print('This is 1')
        
    case 3:
        print('This is 3')
    
    case _:
        print('This is default case') # match anything that doesn't match the above cases

    