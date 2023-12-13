import operator

catalog = {'green table': 5000, 'brown chair': 1500, 'blue sofa': 15000, 'wardrobe': 10000}


# Sorting by name
catalog_sorted_by_key = dict(sorted(catalog.items(), key=operator.itemgetter(0)))# operator returns the item by its index

print(catalog_sorted_by_key)
# {'blue sofa': 15000, 'brown chair': 1500, 'green table': 5000, 'wardrobe': 10000}

# Sorting by value
catalog_sorted_by_value = dict(sorted(catalog.items(), key=operator.itemgetter(1))) 
print(catalog_sorted_by_value)  
# {'brown chair': 1500, 'green table': 5000, 'wardrobe': 10000, 'blue sofa': 15000}

# Sorting by reversed value
catalog_sorted_by_value = dict(sorted(catalog.items(), key=operator.itemgetter(1), reverse=True))
print(catalog_sorted_by_value)  
# {'blue sofa': 15000, 'wardrobe': 10000, 'green table': 5000, 'brown chair': 1500}