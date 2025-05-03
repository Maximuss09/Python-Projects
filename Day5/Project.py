import random

letters = ['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#',  '$', '%', '&', '/', '(', ')', '+', '*']

print("Welcome to the pasword generator like Google when you trying to set a new password lol")
nr_letter = int(input("Numbers of letters you want? "))
nr_symbols = int(input("Numbers of symbols you want? "))
nr_numbers = int(input("Numbers of numbers you want? "))

#   --------EASY WAY--------
# password = ""

# for char in range(0, nr_letter):
#     password += random.choice(letters)
# for char in range(0, nr_numbers):
#     password += random.choice(symbols)
# for char in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(password)


#   ----HARD AND CORRECT WAY----

password_list = []

for char in range(0, nr_letter):
    password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

print (f"Your password would be: {password}")


