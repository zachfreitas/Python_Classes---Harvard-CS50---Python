# Ask the user for their name.
# Remove Whitespace from string and Use title case the string.
name = (
    input("What's your name? ")
    .strip() # Strip extra spaces
    .title() # Use Propercase
    )

# Split users name into first and last name
first, last = name.split(" ")

# Say hello to user.
print(f"\nHi {first}!")
print("\nHi " + name + "!")
print("\nHi", name, "!")