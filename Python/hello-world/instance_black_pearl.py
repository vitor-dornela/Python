class Ship:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.cargo = 0
        self.captain = None

    def name_captain(self, cap):
        self.captain = cap
        print("{} is the captain of the {}".format(self.captain, self.name))
    
    def load_cargo(self, weight):
        if weight <= self.free_space():
            self.cargo += weight
            print("Loaded {} tons".format(weight))
        else:
            print("Cannot load that much")

    def unload_cargo(self, weight):
        if self.cargo - weight >= 0:
            self.cargo -= weight
            print("Unloaded {} tons".format(weight))
        else:
            print("Cannot unload that much")
    
    def free_space(self):
        return self.capacity - self.cargo

        
black_pearl = Ship("Black Pearl", 800)
black_pearl.name_captain("Jack Sparrow") # prints "Jack Sparrow is the captain of the Black Pearl"
print(black_pearl.captain)  # "Jack Sparrow"


# example
black_pearl.load_cargo(600)
# "Loaded 600 tons"

black_pearl.unload_cargo(400)
# "Unloaded 400 tons"

black_pearl.load_cargo(700)
# "Cannot load that much"

black_pearl.unload_cargo(300)
# "Cannot unload that much"