planets = {'Venus', 'Earth', 'Jupiter'}  
  
# initializing by default with None 
planets_dict = dict.fromkeys(planets)
print(planets_dict)  # {'Jupiter': None, 'Venus': None, 'Earth': None}

# initializing with a value
value = 'planet'
planets_dict = dict.fromkeys(planets, value)
print(planets_dict)  # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'planet'}

# changing the value of 'Jupiter'
planets_dict['Jupiter'] = "giant " + planets_dict['Jupiter']
print(planets_dict)
 # {'Earth': 'planet', 'Venus': 'planet', 'Jupiter': 'giant planet'}

testable = {'September': '16°C', 'December': '-10°C'} 
another_dictionary = {'June': '21°C'}

# adding items from another dictionary
testable.update(another_dictionary)
print(testable)  # {'September': '16°C', 'December': '-10°C', 'June': '21°C'}

# adding a key-value pair
testable.update(October='10°C')
print(testable)  
# {'September': '16°C', 'December': '-10°C', 'June': '21°C', 'October': '10°C'}

testable = {'September': '16°C', 'December': '-10°C'}
testable.update(December='-20°C')

print(testable)  # {'September': '16°C', 'December': '-20°C'}


