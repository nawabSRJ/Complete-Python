# ? Syntax : dictionary = {key:expression for (key,value) in iterable}

# ? with condition : dictionary = {key:expression for (key,value) in iterable if condition}

# ? condition for value in expression : {key:(if/else) for (key,value) in iterable}

# ? for complex logic we can also add function call : dictionary = {key: function(value) for (key,value) in iterable}



# example 1 : change the temperature from fahrenheit to celcius from one dict to another
cities_F = {'New York' : 32, 'Boston':75,'Chicago' : 50}

cities_C = {key: round((value-32)*(5/9)) for (key,value) in cities_F.items()}

print(cities_C) # created a whole new dictionary using dict comprehension

# todo : from the existing dict weather below, make a new dict using dict comprehension that has only the cities with weather sunny

weather = {'New York' : 'Sunny', 'Boston':'Sunny', 'Los Angeles' : 'Cloudy', 'Chicago':'Rainy'}

sunny_city = {key:value for (key,value) in weather.items() if value == 'Sunny'}
print(sunny_city)

# ? When we have to choose the value based on a condition then we can put the if/else in the expression itself

cities = {'New York':32, 'Boston':75, 'Chicago' : 50}

desc_cities = {key:("WARM" if value >= 40 else "COLD") for (key,value) in cities.items()}
print('Description of cities : ', desc_cities)

# todo : use a function call now
# using the old cities dict as original

def check_temp(val):
    if val >= 40:
        return "WARM"
    else:
        return "COLD"

desc_cities = {key:check_temp(value) for (key,value) in cities.items()}
print('Description of cities (function) : ', desc_cities)


