# ? We are here only solving the problem mentioned in the third.py file at last
import time

def timer_dec(base_fn):
    def enhanced_fn(*args, **kwargs):
        start_time = time.time()
        base_fn(*args, **kwargs)
        end_time = time.time()
        print(f'Time taken : {end_time - start_time} seconds')
    return enhanced_fn


@timer_dec
def brew_tea(tea_type, steep_time):
    print(f'Brewing {tea_type} tea')
    time.sleep(steep_time)
    print(f'{tea_type} tea ready!')


brew_tea('Black',1) # positional arguments, NOT keyword args
brew_tea(tea_type='Green', steep_time=2) # Keyword Arguments

# ! The problem : so far our base functions only use print statements and don't return anything, so how do we handle this in our decorator functions, what if the make_matcha() function returns something at the end?? At the same time, can the brew_tea() function be same and still be compatible with decorator timer_dec
# * Yes, it can be, refer file fifth.py