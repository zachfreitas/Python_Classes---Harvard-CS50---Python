# Dictionary Comprehension

students = ["Hermione", "Harry", "Ron"]

# Version One
# gryffindors = []

# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
#[{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]


# Version Two - List Comprehension
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
#[{'name': 'Hermione', 'house': 'Gryffindor'}, {'name': 'Harry', 'house': 'Gryffindor'}, {'name': 'Ron', 'house': 'Gryffindor'}]
    
    
# Version 3 - Dictionary Comprehension
gryffindors = {student: "Gryffindor" for student in students}
#{'Hermione': 'Gryffindor', 'Harry': 'Gryffindor', 'Ron': 'Gryffindor'}
print(gryffindors)

