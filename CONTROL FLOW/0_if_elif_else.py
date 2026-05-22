# Conditional Statements are based on the correctness of the condition
# if, elif (else if) else are used in python for this

age = int(input('Enter Age : '))

if age<=16:
    print('Cannot Apply')
elif age> 16 and age < 25:
    print('Apply')
else:
    print('Overage')

# Nested Conditions

if age >= 18:
    name = input('Enter name : ')
    if(len(name) < 3):
        print('Eligible for Re-naming')
    else:
        print('No need for Re-naming')
elif age < 18 and age >= 10:
    print('Not the right age')
else:
    print('Can re-name automatically')

# Short Hand if-else
print('Eligible for Re-naming') if len(name) < 3 else print('No need for Re-naming')


# more examples on this : 
a = 5
b = 5
c = 7
print(9) if a > b else print(-9) 

print("A") if a > b else print("=") if a == b else print("B") if a < c else print("ghanta")