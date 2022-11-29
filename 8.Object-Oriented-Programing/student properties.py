class Student:
    def __init__(self, name, house) -> None:
        self.name = name
        self.house = house
        
    # Printing
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    # Getter
    @property
    def name(self):
        return self._name
    # Setter
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    # Getter
    @property
    def house(self):
        return self._house
    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house



def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house) # Constructor Clause. It instantiates a Student class object.


if __name__ == "__main__":
    main()

# Harry
# Gryffindor
# ["Gryffindor","Ravenclaw","",""]
# Padma
# Ravenclaw