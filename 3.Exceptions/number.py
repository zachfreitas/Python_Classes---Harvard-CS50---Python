
# Error Handling
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            y = input("Enter an integer: ")
            x = int(y)
        except ValueError:
            # pass
            print(f"'{y}' is not an integer")
        else:
            break
    return x

main()