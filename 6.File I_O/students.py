# # with open("students.csv", "r") as file:
# #     for line in file:
# #         # row = line.rstrip().split(",")
# #         # or
# #         name, house = line.rstrip().split(",")
# #         # print(f"{row[0]} is in {row[1]}")
# #         print(f"{name} is in {house}")


# students = []

# with open("students.csv", "r") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name":name, "house":house}
#         students.append(student)

# # def get_name(student):
# #     return student["name"]

# # def get_house(student):
# #     return student["house"]

# # for student in sorted(students, key = get_name, reverse=False):
# #     print(f"{student['name']} is in {student['house']}")

# for student in sorted(students, key = (lambda student: student["name"]), reverse=False):
#     print(f"{student['name']} is in {student['house']}")
    
# import csv
# students = []

# with open("students.csv", "r") as file:
#     reader = csv.reader(file)
#     for name, house in reader:
#         students.append({"name": name, "house": house})


# for student in sorted(students, key = (lambda student: student["name"]), reverse=False):
#     print(f"{student['name']} is in {student['house']}")

import csv
students = []

with open("studentsdict.csv", "r") as file:
    reader = csv.DictReader(file, fieldnames=['name', 'house', 'home'])
    for row in reader:
        students.append({"name": row["name"], "house": row["house"], "home": row["home"]})


for student in sorted(students, key = (lambda student: student["name"]), reverse=False):
    print(f"{student['name']} is in {student['house']} and lives at {student['home']}")