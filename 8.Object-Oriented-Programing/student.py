class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house

    # Printing
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house) # Constructor Clause. It instantiates a Student class object.
    

def main():
    student = Student.get()
    print(student)

if __name__ == "__main__":
    main()

# Harry
# Gryffindor
# ["Gryffindor","Ravenclaw","",""]
# Padma
# Ravenclaw