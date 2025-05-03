import random
import DAY04_mymodule

random_integrer = random.randint(a=2, b=21)

print(random_integrer)
print(DAY04_mymodule.my_module)
#------------------------------------------------------------

# random_number = random.random() * 10
# print(random_number)

# random_float = random.uniform(1, 10)
# print(random_float)

# -----------------------------------------------------------
# random_h_or_t = random.randint(0, 1)
# if random_h_or_t == 0:
#     print("Heads")
# else:
#     print("Tails")
# -----------------------------------------------------------
# LISTS
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(random.choice(friends))

random_name = random.randint(0, 4)
print(friends[random_name])

# if random_name == 0:
#     print(friends[-1])
# elif random_name == 1:
#     print(friends[0])
# elif random_name == 2:
#     print(friends[1])
# elif random_name == 3:
#     print(friends[2])
# elif random_name == 4:
#     print(friends[3])
# else:
#     print("All of them")

# -------------------------------------------------------
# NESTED LISTS

# fruits = ["Strawberries", "Nectarines","Apples", "Grapes","Peaches", "Cherries", "Pears" ]
# vegetables= ["Spinach","Kale", "Tomatoes", "Celery", "Potatos"]

# dirty_dozen = [fruits, vegetables]
# print(dirty_dozen[1][1])


