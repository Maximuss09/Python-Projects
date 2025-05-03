# # ---------- DEBUGS --------------

# def function():
#     for i in range(1, 20):
#         if i == 20:
#             print("You Got it")

# function()

# # Describe the problem: 
# # 1. What is the For loop doing?
# # 2. When is the function meant to print "You Got it"?
# # 3. What are your assumption about the value of i?:

# # --------- FIXED DEBUG -----------


# def function():
#     for i in range(1, 21):
#         if i == 20:
#             print("You Got it")

# function()

# # ----------------------------------

# year = int(input("What is your year of birht? "))

# if year > 1988 and year < 1994:
#     print("You are a millenial. ")
# elif year > 1994:
#     print("You are a Gen Z")
# #             ---

# year = int(input("What is your year of birht? "))

# if year > 1988 and year <= 1994:
#     print("You are a millenial. ")
# elif year > 1994:
#     print("You are a Gen Z")


# # ------------------------------------

# age = int(input("How old are you? "))

# if age > 18:
#     print(f"You can drive at age {age}")

# #           ---------

# try: 
#     age = int(input("How old are you? "))

# except ValueError:
#     print("You have typed in an invalid caracter. Try again with a numerical response such as 10.")
#     age = int(input("How old are you? "))

# if age > 18:
#     print(f"You can drive at age {age}")


# --------------------------------------

word_per_page = 0

pages = int(input("Number of page: "))
word_per_page = int(input("Number of word per page: "))
total_words = pages*word_per_page
print(total_words)


# ---------------------------------------
