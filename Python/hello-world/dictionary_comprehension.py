planets_diameter_km = {'Earth': 12742, 'Mars': 6779}

# correct but long way
planets_diameter_mile = {}
for key, value in planets_diameter_km.items():
    planets_diameter_mile[key] = round(value / 1.60934, 2)

print(planets_diameter_mile)  # {'Earth': 7917.53, 'Mars': 4212.29}

# convenient and short!
planets_diameter_mile = {key: round(value / 1.60934, 2) for (key, value) in 
                         planets_diameter_km.items()}

print(planets_diameter_mile)  # {'Earth': 7917.53, 'Mars': 4212.29}

# you can create conditions 
planets_diameter_mile = {key: round(value / 1.60934, 2) for (key, value) in planets_diameter_km.items() if value > 10000}

print(planets_diameter_mile)  # {'Earth': 7917.53}