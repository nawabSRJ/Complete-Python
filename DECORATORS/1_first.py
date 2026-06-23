# todo : simple example to explain decorators, you may also refer info.png

# ? The task of a decorator is to take a base_function and enhance it and later return it, enhancing is also termed as 'decorating'

# ! This decoration could have been done within the same function, why use decorators?
# ? Because that destroys the 'principle of single responsibility' and if that decoration is needed in many functions then we need to write the same 'decoration' code in all of them which leads to code redundancy, thereby impacting code maintainability

# * example : brew_tea and make_matcha while also telling how much time each of them takes ~ a simple example that can help us understand how decorators work

import time


# decorators take the function in args that they enhance
def timer_dec(base_fn):
    def enhanced_fn():
        start_time = time.time()
        base_fn()
        end_time = time.time()
        print(f'Time taken : {end_time - start_time} seconds')
    return enhanced_fn  # the enhanced function is always returned otherwise the decorator won't work at all and returns None thus an ERROR

# * decorators are declared first before the actual function on which they are used

@timer_dec
def brew_tea():
    print('Brewing Tea....')
    time.sleep(1)
    print('Tea is Ready!')


# * Now by default whenever we call the brew_tea function it will be going through the decorator
brew_tea()

# * Now using the timer_dec for any other function is also possible thus reducing code redundancy

@timer_dec  # just add the decorator like this
def make_matcha():
    print('Making Matcha....')
    time.sleep(1)
    print('Matcha is Ready!')

make_matcha()
# TODO : In second.py we will see how to use decorators with functions who have arguments




