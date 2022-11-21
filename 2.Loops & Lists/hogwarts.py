
students = ["Hermione", "Harry", "Ron"]


print(students[0])
print(students[1])
print(students[2])
print(students[:])


print("\n"*3)

for student in students:
    print(student)


for i, student in enumerate(students):
    print(student)
    
    

for i in range(len(students)):
    print(i + 1, students[i])



# Dictionaries 
# Key & Values

students = ["Hermione", "Harry", "Ron", "Draco"]
house = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


students = {"Hermione":"Gryffindor",
            "Harry":"Gryffindor", 
            "Ron":"Gryffindor", 
            "Draco":"Slytherin"}

print(students["Hermione"])
print(students["Draco"])

# iterate over the keys
for student in students:
    print(student, students[student], sep=", ")
    



# List of dictionaries
students = [
    {"name": "Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus":"Jack Russell Terrier"},
    {"name": "Draco", "house":"Slytherin", "patronus":None}
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")
