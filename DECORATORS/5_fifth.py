import time
from datetime import datetime, timedelta
def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        result = base_fn(*args, **kwargs)
        end_time = time.time()
        print(f'Time taken : {end_time - start_time} seconds')
        return result
    return enhanced_fn


@timer_dec
def brew_tea(tea_type, steep_time):
    print(f'Brewing {tea_type} tea')
    time.sleep(steep_time)
    print(f'{tea_type} tea ready!')


@timer_dec  
def make_matcha():
    print('Making Matcha....')
    time.sleep(1)
    print('Matcha is Ready!')
    return f'Drink matcha by {datetime.now() + timedelta(minutes=30)}'

brew_tea('Black',1) # positional arguments, NOT keyword args
brew_tea(tea_type='Green', steep_time=2) # Keyword Arguments
make_matcha()   # will only show print statements
# * Now as usual only calling the make_matcha() function is not enough, since it returns a value we need to print that as well
print('\n\n')
print(make_matcha())

# * The brew_tea function doesn't return anything so yeah no problem but what if we still try to print it, because in the timer_dec function we are still trying to return the result inside the enhanced_fn

print('\n\n')
print(brew_tea('Lemon',1))  # No error, returns None


# * Notes:
# Decorators can decorate functions with any number of positional and keyword arguments(thanks to *args and **kwargs).

# Decorators also support functions that return values without breaking when used with functions that don't.
