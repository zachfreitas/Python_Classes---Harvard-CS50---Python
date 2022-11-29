import re

url = input("URL: ").strip()


# username = url.replace("https://twitter.com/", "")
# print(f"Username: {username}")

# username = url.removeprefix("https://twitter.com/")
# print(f"Username: {username}")

# Find and replace
# username = re.sub("(https?://)?(www\.)twitter\.com/", "", url)
# print(f"Username: {username}")

if matches := re.search("^(?:(?:.+)/)*(.+)$", url, re.IGNORECASE):
    print(f"Username: {matches.group(1)}")

#^
# tests:
# https://twitter.com/davidmalan


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