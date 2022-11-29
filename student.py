class Student:
    def __init__(self, name, house, patronus) -> None:
        if not name:
            # print("Missing name")
            # sys.exit("Missing name") # Extreme
            raise ValueError("Missing Name")
        if house not in ["Gryffindor","Ravenclaw","Hufflepuff","Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    def charm(self):
        match self.patronus:
            case "Stag":
                return "🦌"
            case "Otter":
                return "🦦"
            case "Jack Russel Terrier":
                return "🐶"
            case _:
                return "🪄"


# def main():
#     student = get_student()
#     if student[0] =="Padma":
#         student[1] = "Ravenclaw"
#     print(f"{student[0]} from {student[1]}")

# def main():
#     name, house = get_student()
#     print(f"{name} from {house}")

# Returns a Tupple
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return name, house # or (name, house)

# Returns a list.
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return [name, house]

# def main():
#     student = get_student()
#     # if student["name"] =="Padma":
#     #     student["house"] = "Ravenclaw"
#     print(f"{student['name']} from {student['house']}")

# Returns Student
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return {"name": name, "house": house}

# # Returns Student
# def get_student():
#     return {"name": input("Name: "), 
#             "house": input("House: ")}


def main():
    student = get_student()
    # if student["name"] =="Padma":
    #     student["house"] = "Ravenclaw"
    # print(f"{student.name} from {student.house}")
    print("Expecto Patronum")
    print(student.charm())

# def get_student():
#     student = Student()
#     student.name = input("Name: ")
#     student.house = input("House: ")
#     return student

def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus) # Constructor Clause. It instantiates a Student class object.


if __name__ == "__main__":
    main()

# Harry
# Gryffindor
# ["Gryffindor","Ravenclaw","",""]
# Padma
# Ravenclaw