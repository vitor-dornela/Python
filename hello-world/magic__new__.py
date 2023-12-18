class Puppy:
    n_puppies = 0  # number of created puppies

    def __new__(cls): # __ are also called "dunders"
        if cls.n_puppies < 3: # limit the total number of puppies
            cls.n_puppies += 1
            return object.__new__(cls)  
puppy1 = Puppy()
puppy2 = Puppy()
puppy3 = Puppy() 
puppy4 = Puppy() # None
print(puppy1, puppy2, puppy3, puppy4)