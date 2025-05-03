"""FILENOTFOUND"""
# with open ("a_file.txt")as file:
#     file.read()

"""KEY ERROR"""
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existing_key"]

"""INDEX ERROR"""
# fruit_list = ["Apple", "Banana", "Pear"] #INDEX: [0, 1, 2]
# fruit = fruit_list[3]

"""TYPE ERROR"""
# text = "abc"
# print(text + 3)

# -----------------------------------------------------------

"""FILENOTFOUND"""

# try:
#     file = open ("a_file.txt")
# except:
#     print("There was a error")


# ----------------------------------------------------------

# height = float(input("Height: "))
# weight = int(input("Weight: "))

# if height >3:
#     raise ValueError("Human Height should not be over 3 meters.")

# BMI = weight / height**2
# print(BMI)



# -------------------------------------------------------
"""TEST 1"""

fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit pie")
    else:
        print(fruit + "pie")

make_pie(4)

# ----------------------------------------------------
"""TEST 2"""

facebook_posts = [
    {'Likes': 21, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3}
]


def count_likes(posts):

    total_likes = 0
    for post in posts:
        
       try:
        total_likes = total_likes + post['Likes']
       except KeyError:
        pass 
    
    return total_likes


count_likes(facebook_posts)
