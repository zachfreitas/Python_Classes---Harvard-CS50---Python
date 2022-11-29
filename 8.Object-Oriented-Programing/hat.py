import random

class Hat:
    # Class Variable
    houses = ["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"]
    
    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))

Hat.sort("Harry")

# if __name__ == "__main__":
#     main()