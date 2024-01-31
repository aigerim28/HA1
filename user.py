# Q3- Write a program user.py that stores information about a user into a dictionary, and performs exactly as given.

user_info = {}

user_info["name"] = input("What is the user's name? ")
user_info["age"] = int(input("What is the user's age? "))
user_info["country"] = input("What is the user's country of birth? ")
user_info["known for"] = input("What is the user known for? ")

print(user_info)