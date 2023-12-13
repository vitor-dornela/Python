# Let's create a list of some gifts in Santa's bag
gifts = ['Toy Train', 'Teddy Bear', 'Doll', 'Candy Cane']

# Add a new gift to the list
gifts.append("Book of Fairytales")

# Print the list after adding the new gift
print("Santa's Bag of Gifts: " + ', '.join(gifts) + '\n') # join will only work with strings
# Santa's Bag of Gifts: Toy Train, Teddy Bear, Doll, Candy Cane, Book of Fairytales

# Add a number to the list
gifts.append(1)

# Print the list after adding the number
print("Santa's Bag of Gifts: " + ', '.join(str(gifts) for gifts in gifts) + '\n') 
# Santa's Bag of Gifts: Toy Train, Teddy Bear, Doll, Candy Cane, Book of Fairytales, 1