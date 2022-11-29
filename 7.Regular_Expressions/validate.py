import re 

email = input("What's your email? ").strip()

# if "@" in email and "." in email:
#     print("Valid")
# else:
#     print("Invalid")
    
    
# username, domain = email.split("@")

# # if username and "." in domain:
# #     print("Valid")
# # else:
# #     print("Invalid")

# if username and domain.endswith(".edu"):
#     print("Valid")
# else:
#     print("Invalid")

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


# r"" are considered raw strings

# pattern = r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$"
pattern = r"^\w+@(\w+\.)+(com|edu|gov|biz)$"
pattern = r""
# pattern = r"^[^@]+@[^@]+\.edu$"
if re.search(pattern, email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")