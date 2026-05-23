# TODO : Use a same decorator for one function with args and another with no args
# * Note to understand : *args in function header packs the no. of positional arguments in a tuple but the same syntax when used in a function call - then it unpacks the tuple into positional arguments - Same Syntax, Different Places - Different Job

import time

def timer_dec(base_fn):
    def enhanced_fn(*args):
        start_time = time.time()
        base_fn(*args)
        end_time = time.time()
        print(f'Time taken : {end_time - start_time} seconds')
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

brew_tea('Green',2)
make_matcha()


# ! The Problem : here if we try to pass keyword arguments in the brew_tea() function then it will break, *args is NOT meant to handle keyword arguments
brew_tea(tea_type='Green', steep_time=1)    # Unexpected keyword argument error

# * To solve this problem we can use **kwargs ~ refer file fourth.py