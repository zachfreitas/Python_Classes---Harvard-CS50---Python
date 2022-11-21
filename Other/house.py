name = input("What's your name? ")

# if name =="Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")



match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")