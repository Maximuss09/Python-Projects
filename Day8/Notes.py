# def greet():
#     print("hello")
#     print("hello")
#     print("hello")

# greet()
# ------------------------------------
# FUNCTION THAT ALLOW FIR INPUT

# def greet_with_name(name): # name es una variable. Se crea una nueva variable en donde su valor se define cuando se llama a la funcion
#     print(f"hello {name}") # en programacion se le conoce con el nombre "Parameter" a la variable que creamos en esta funcion. El parametro es el nombre del dato que queremos utilizar y se utiliza dentro de la funcion que creamos
#     print(f"hello {name}")
#     print(f"hello {name}")

# greet_with_name("adam") # lo que se ponga entre parentesis es a lo que equivale la variable creada en nuestra funcion.
#                         # en programacion se le conoce con el nombre "Argument" a aquel valor de la variable que creamos o al "Parameter". El argumento es el Dato que va a utilizar la variable cuando sea llamada    
#----------------------------------- 
# TEST

# user_age = int(input("What is your age? "))

# def life_in_weeks(convertion =  4696 - (user_age*52)):
#     print(f"You have {convertion} weeks left")

# life_in_weeks()
# -------------------------------------

# def greet_with (name, location):
#     print(f"hello {name}")
#     print(f"what is it like in {location}")


# greet_with(name="karina", location="uk") 
# greet_with(location="uk",name="karina") 

# --------------------------------------
#    TEST 2 

# def calculate_love_score(name1, name2):
#     combined_names = (name1 + name2).lower()
#     print(combined_names)
#     true_score = sum(combined_names.count(char) for char in "true")
#     love_score = sum(combined_names.count(char) for char in "love")
#     love_score_str = str(true_score) + str(love_score)
#     love_score_str1 = true_score + love_score
#     print(love_score_str1)
#     print(int(love_score_str))


# calculate_love_score(name2="alberto", name1="daniela")


# ------------------------------------------





