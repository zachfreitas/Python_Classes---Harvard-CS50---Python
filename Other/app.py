# This is class code
###############################
# Story
# name = input("Enter your name: ")
# age = input("What is your age: ")
# print(f"There once was a man named {name}, ")
# print(f"he was {age} years old. ")
# print(f"He really liked the name " + name + ", ")
# print(f"but didn't like being {age}.")

# Calculator
# num1 = input("Enter a number: ")
# num2 = input("Enter a number: ")

# result = float(num1) + float(num2)
# print(result)

###############################
# # Madlibs Exercise
# color = input("enter a color: ")
# plural_noun = input("Enter a plural noun: ")
# celebrity = input("Enter a Celebrity: ")

# print(f"Roses are {color}")
# print(f"{plural_noun} are blue")
# print(f"I love {celebrity}")

###############################
# # Functions
# # Create function
# def sayhi():
#     print("Hello User")

# # run function
# sayhi()

# # Function with parameters
# # Create function
# def sayhi(name, age):
#     print(f"\nHello {name} you are {age}")

# # run function
# sayhi(input("Enter your name: "), input("What is your age: "))


###############################
# Function with parameters
# Create function
# def cube(num):
#     result = num * num * num
#     return print(result)

# # run function
# cube(3)


###############################
# If Statements in python

# is_male = False
# is_tall = False

# if is_male and is_tall:
#     print("You are a tall Male")
# elif is_male and not(is_tall):
#     print("You are a short male.")
# elif not(is_male) and is_tall:
#     print("You are a tall female.")
# else:
#     print("You are short female")
    

    
###############################    
# # Build Advance Calculator
# num1 = float(input("Enter first number: "))
# op = input("Enter operator: ")
# num2 = float(input("Enter second number: "))


# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "/":
#     print(num1 / num2)
# elif op == "*":
#     print(num1 * num2)
# else:
#     print("Invalid operator")

###############################
# Dictionaries

# monthConversions = {
#     "jan": "january",
#     "feb": "february",
#     "mar": "march",
#     "apr": "april",
#     "may": "may",
#     "jun": "june",
# }


# print(monthConversions[input("Enter first number: ").lower()].title())


# print(monthConversions.get(input("Enter first number: ").lower(), "Not a valid key").title())


# ###############################
# # While Loop

# i = 1
# while i <= 10:
#     print(i)
#     i += 1

    
# print("Done with loop")



# ###############################
# # Building a Guessing Game

# secret_word = "giraffe"
# guess = ""
# guess_count = 0
# guess_limit = 3
# out_of_guesses = False

# while guess != secret_word and not(out_of_guesses):
#     if guess_count < guess_limit:
#         guess = input("Enter guess: ").lower()
#         guess_count += 1
#     else: 
#         out_of_guesses = True

# if out_of_guesses:
#     print("You lose!")
# else:
#     print("You win!")
    
# ###############################    
# # For Loop

# for letter in "Giraffe Academy":
#     print(letter)
    
    
# friends = ["Jim", "Karen", "Kevin"]

# for name in friends:
#     print(name)
    
    
# for index in range(3, 10, 2):
#     print(index)
    
    
# for index in range(len(friends)):
#     print(friends[index])
    

    
# for index in range(5):
#     if index == 0:
#         print("First Iteration")
#     else:
#         print("Not First Iteration")


# ###############################   
#exponet function

# def raise_to_power(base_num, power_num=1):
#     result = 1
#     for index in range(power_num):
#         result = result * base_num
#     return result


# print(raise_to_power(3, 3))


# ###############################   
# Nested Loops & 2 Dimensional List

# # 2 Dimensional List
# number_grid = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
#     [0]    
# ]

# print(number_grid[0][0])
# print(number_grid[3][0])

# for row in number_grid:
#     for col in row:
#         print(col)



################################
# Basic Translator

# """
# Poop
# peepee
# what
# """

# def translate(phrase):
#     translation = ""
#     for letter in phrase:
#         if letter.lower() in "aeiou":
#             if letter.isupper():
#                 translation = translation + "G"
#             else:
#                 translation = translation + "g"
#         else:
#             translation = translation + letter
#     return translation


# print(translate(input("Enter a phrase: ")))



# ################################
# # Comments

# """
# Multiline Comments
# Poop
# peepee
# what
# """


######################################
# Try Excepts

# def get_int():
#     number = int(input("Enter a number: "))
#     print(number)

# try:
#     get_int()
# except ZeroDivisionError as err:
#     print("Divided by Zero")
# except ValueError:
#     print("Invalid Input, enter Int.")



######################################
# Modules

# from usefultools import roll_dice

# print(roll_dice(int(input("Enter a number: "))))



###############################################
# Classes and Objects

# Classes allow you to define your own datatype


# from Student import Student

# student1 = Student("Bill", "Economics", 3.84, False)


# print(student1,"\n")


# print("Student Name:",student1.name,"\n")
# print("Student GPA:",student1.gpa,"\n")




###############################################
# Classes and Objects - Quiz example

# from Question import Question

# question_prompts = [
#     "What color are Apples?\n(a) Red\n(b) Yellow\n(c) Orange\n\n",
#     "What color are Bananas?\n(a) Red\n(b) Yellow\n(c) Orange\n\n",
#     "What color are Strawberries?\n(a) Red\n(b) Yellow\n(c) Orange\n\n"]

# # answer_key = [
# #     q1 = Question(question_prompts[0], "a"), q2 = Question(question_prompts[1], "b"), q3 = Question(question_prompts[2], "a"),
# # ]
# print(question_prompts[0])
# b = Question()
# b("poop",'a')
# print(b.answer)

# # def run_test(answer_key):
# #     score = 0
# #     for question in answer_key:
# #         answer = input(question.prompt)
# #         if answer == question.answer:
# #             score += 1
# #     print("You got" + str(score) + "/" + str(len(questions)) + " correct")
    
# # run_test(questions)