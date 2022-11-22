
# File I/O
# 
# name = input("What's your name? ")
# file =  open("names.txt", "a")
# file.write(f"{name}\n")
# file.close

# or 
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")


# with open("names.txt", "r") as file:
#     lines = file.readlines()
    
# for line in lines:
#     print("Hello,", line.rstrip())
    
    
    
with open("names.txt", "r") as file:
    for line in sorted(file,reverse=True):
        print("Hello,", line.rstrip())