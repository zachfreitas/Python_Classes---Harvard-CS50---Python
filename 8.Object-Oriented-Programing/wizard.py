class Wizard:
    def __init__(self, name) -> None:
        if not name:
            raise ValueErro("Missing name")
        self.name = name 

class Student(Wizard):
    def __init__(self, name, house) -> None:
        supper().__init__(name)
        self.house = house


class Professor(Wizard):
    def __init__(self, name, subject) -> None: 
        supper().__init__(name)
        self.subject = subject
        
        
wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")