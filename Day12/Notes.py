# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function {enemies}")


# increase_enemies()
# print(f"enemies outside function: {enemies}")



# ------- LOCAL SCOPE---------

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# -------- GLOBAL SCOPE -------

player_health = 10


def game():

    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

game()
print(player_health)

# Si creas una variable dentro de una funcion, 
# entonces solo estara disponible dentro de esa funcion. 
# Pero si creas una variable dentro de un bloque If o While loop o For loop, 
# entonces eso no cuenta como  crear un Local Scope separado
#


#------------------------------------------------------------

# There is not such thing as Block Sscope in Python!


# game_level = 3
# enemies = ["Skeleton", "Zombie", "Alien"]


# if game_level < 5:              # Block como If, While, For, todos es tos bloques no cuentan como LOCAL SCOPE
#     new_enemy = enemies[0]

# print(new_enemy)


#------------- QUIZ ------------------

# def is_prime(num):
    
#     if num < 1:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False

#     return True
# print(is_prime(5))
# print(is_prime(10))

# ------------------------------------

# Global Constants









