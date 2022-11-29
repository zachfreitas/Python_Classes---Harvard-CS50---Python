# Constants

# example 1

# MEOWS = 3 # Capitialize to show this is expected to be constant.

# for _ in range(MEOWS):
#     print("meow")
    
    
# example 2
class Cat:
    MEOWS = 3
    
    def meow(self):
        for _ in range(Cat.MEOWS):
            print("meow")

cat = Cat()
cat.meow()


