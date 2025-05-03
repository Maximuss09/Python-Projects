import random
import math

# def mutate (a_list):
#     b_list = []
#     new_item = 0
#     for item in a_list:
#         new_item = item*2
#         new_item += random.randint(1, 3)
#         new_item = math.add(new_item, item)
#     b_list.append(new_item)
#     print(b_list)


# mutate({1, 2, 3, 5, 8, 13})


# ---------------

def mutate (a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item*2
        new_item += random.randint(1, 3)
        new_item = math.add(new_item, item)
        b_list.append(new_item)
    print(b_list)


mutate({1, 2, 3, 5, 8, 13})



# --------------

"""TAKE AWAYS:
1. Take a Brake
2. Ask a Friend
3. Run the program Often
4. Ask on StackOverflow


"""





# https://replit.com/@appbrewery/higher-lower-final-debugged?v=1#game_data.py