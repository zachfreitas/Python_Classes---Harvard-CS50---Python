import re

name = input("What's your name? ").strip()

# if "," in name:
#     last, first = name.split(", ")
#     name =f"{first} {last}"
# print(f"Hello, {name}")


if matches := re.search(r"^(.+), *(.+)$", name):
    # last, first = matches.groups() # or
    last = matches.group(1)
    first = matches.group(2)
    name =f"{first} {last}"
print(f"Hello, {name}")



##################################################
# re # This is a regular expressions library.
##################################################
# . = any character
# * = 0 or more repetitions of thing to the left.
# + = 1 or more repetitions of thing to the left.
# ? = 0 or 1 repetitions of thing to the left.
# {m} = m repetitions of thing to the left.
# {m, n} = m-n range of repetitions of thing to the left.
# ^ = matches the start of the string
# $ = matches the end of the string or just before the newline at the end of the string.
# [] set of characters: examples [a-zA-Z0-9_] aka \w
# [^] complementing the set of characters aka Not
# Common Patterns:
# \d = decimal digit
# \D = not a decimal digit
# \s = white space characters
# \S = Not a white space charager
# \w = word character... as well as numbers and the underscore
# \W = Not a word character.
# A|B = or
# (...) = a group 
# (?:...) = non-capturing version