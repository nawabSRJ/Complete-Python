# TODO : In this file we will primarily explore *args and **kwargs and their use cases
# * As we saw in the Functions_basic.py file we can use an asterick (*) to take any no. of positional arguments as a tuple

# * Note that this can be done even with other default parameters

def brew_tea(cust_name, tea_type, *args):
    print(f'{cust_name} ordered a {tea_type}')
    print('Rest of the arguments are : ', args)

brew_tea('Srajan', 'Black')
brew_tea('Srajan','Black', ('Oat Milk', 'Honey'))

# *args will take any no. of positional arguments, and thus it should be placed at the last, although it can be used in the middle but we then have to combine with keyword arguments
print('\n')
def brew_tea2(cust_name, *args, tea_type):
    print(f'{cust_name} ordered a {tea_type}')
    print('Rest of the arguments are : ', args)

brew_tea2('Srajan','Black', 'Oat Milk', tea_type='Honey') 

# ---------------------------------------------------------------------------

# ! What is the use of **kwargs
# The problem with *args is that it only handles positional arguments and does NOT work with keyword arguments.
# Why do we need keyword arguments? Well, the extra elements that we put in the brew_tea function calls mean what? Say 'Oat', the Oat what exactly? Milk? or Honey?
# To overcome this anonymity problem we can use keyword arguments in the function call like : milk='Oat', sweetner='Honey' but then the *args will NOT work with it and we would have to change the function header to accommodate the keyword args, defying the use of *args
#  To solve this problem we have **kwargs

# So template is : 
# *args - collects extra positional args - in a tuple
# **kwargs - collects extra KeyWord arguments - in a dictionary
print('\n-------------- **kwargs --------------\n')
def tea_order(cust_name, tea_type, **kwargs):
    print(f'{cust_name} ordered {tea_type} tea')
    print('Keyword Args are : ', kwargs) 

tea_order('Srajan','Black', milk='Oat', sweetner='Honey')

# * Note : we can use both of them together but here we must place *args before **kwargs in a function header

def make_matcha(cust_name, *args, **kwargs):
    print('\n---- Matcha Cafe ----')
    print(f'Hello {cust_name}')
    print(f'Your matcha with {args} is ready')
    print(f'Your extra demands {kwargs} will also be added')


make_matcha('Srajan','Oat Milk','Zero Sugar', sweetner='Honey')

# ! Note : Positional Arguments before keyword arguments or in other words Keyword Arguments should always be at last or right most of a function signature/header

# * Also the way * operator and ** operator work in function definition and function call is different ~ refer image args_kwargs.png