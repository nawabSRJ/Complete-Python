# TODO : Use decorators along with parameterized functions
import time


# * Now because the base function brew_tea takes 2 positional args we need to adjust the header of the enhanced_fn in a similar manner to do that

# ! Note : the header of base function impacts the header of enhanced function

def timer_dec(base_fn):
    def enhanced_fn(tea_type, steep_time):
        start_time = time.time()
        base_fn(tea_type, steep_time)
        end_time = time.time()
        print(f'Time taken : {end_time - start_time} seconds')
    return enhanced_fn


@timer_dec
def brew_tea(tea_type, steep_time):
    print(f'Brewing {tea_type} tea')
    time.sleep(steep_time)
    print(f'{tea_type} tea ready!')

brew_tea('Green', 1)

# ! But there is a problem here ~ because we have now used the positional args this timer_dec decorator cannot work anymore with the make_matcha() function, here see it :

@timer_dec  
def make_matcha():
    print('Making Matcha....')
    time.sleep(1)
    print('Matcha is Ready!')

make_matcha()   # error : says missing args

# ! What if you don't want the make_matcha() function to take args and still want to perform that decoration on it, can this be done with the same decorator
# * Yes, it can be with the help of *args and **kwargs ~ refer file third.py