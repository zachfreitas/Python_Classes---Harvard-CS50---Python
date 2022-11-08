
def main():
    # Ask the user for their name.
    # Remove Whitespace from string and Use title case the string.
    first, last = (
        input("What's your name? ")
        .strip() # Strip extra spaces
        .title() # Use Propercase
        .split(" ") # Split users name into first and last name
        )
    # Say hello to user.
    hello(first)
    return


def hello(to="World"):
    print(f"\nHi {to}!")
    return


main()