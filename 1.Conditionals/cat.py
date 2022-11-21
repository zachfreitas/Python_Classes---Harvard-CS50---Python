# Loops
# n = 3
# i = 0
# while i < n:
#     print("Meow")
#     i += 1

# For Loops
# for i in [0,1,2]:
#     print("Meow")

# for i in range(3):
#     print("Meow")

# for _ in range(3):
#     print("Meow")


# print("Meow\n"*3, end="")

# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break


# # List Comprehension
# [print("Meow") for _ in range(n)]



def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    [print("Meow") for _ in range(n)]


main()