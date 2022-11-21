
def main():
    # print_column(3)
    # print_row(4)
    print_square(3)
    print_squarex(5)
    
def print_column(height):
    for _ in range(height):
        print("#")
        
def print_row(width):
    print("?" * width)
        
def print_square(size):
    # Outter Loop - For each row in a square
    for i in range(size):
        # Inner Loop - For each brick in a row
        for j in range(size):
            print("#", end="")
        print()


def print_squarex(size):
    # Outter Loop - For each row in a square
    for i in range(size):
        # Inner Loop - For each brick in a row
        print_row(size)

main()