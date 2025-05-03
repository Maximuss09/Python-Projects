
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar (original_text, shift_amount, function_to_do):
    cipher_text = ""
    if function_to_do == ("encode"):
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:
                shifted_position = alphabet.index(letter)+shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            
        print(f"Here is the encoded result: {cipher_text}")
    elif function_to_do == ("decode"):
        for letter in original_text:
            if letter not in alphabet:
                cipher_text += letter
            else:   
                shifted_position = alphabet.index(letter)-shift_amount
                shifted_position %= len(alphabet)
                cipher_text += alphabet[shifted_position]
            
        print(f"Here is the decoded result: {cipher_text}")
    else:
        print("you hace to chose 'encode' or 'decode'")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode to decrypt: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))
    caesar(original_text=text, shift_amount=shift, function_to_do=direction)
    restart = input("Continue? yes or no?")

    if restart == "no":
        should_continue = False
        print("OK bye")




# def encrypt(original_text, shift_amount): # Se crea una funcion con las variables predeterminadas
#     cipher_text = "" # Se crea una variable que almacena las letras que se van cambiando
#     for letter in original_text: # Se crea un for loop para hacer la lectura en cada una de las letras de la palabra introducida
#         shifted_position = alphabet.index (letter) + shift_amount  # Se crea una variable en donde se almacenará el cambio de letra que se haga. Esto se logra con la funcion "index" 
#                                                                    # que devuelve la posicion en la que ocurre el valor especificado, que en el ejemplo de "Hello" seria la letra H, y se le suma la cantidad que almacena la variable shifted_amount
#         shifted_position %= len(alphabet) #Checar como funciona esta funcion. En teoria funciona dividiendo 
#         cipher_text +=alphabet[shifted_position] # Se le suma a la variable cipher_text la letra de la posicion en la cual esta en la posicion que se introducjo en shift
        
#     print(f"Here is the encoded result: {cipher_text}")



# def decrypth(original_text, shift_amount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter)-shift_amount
#         shifted_position %= len(alphabet)
#         cipher_text += alphabet[shifted_position]
#     print (f"Resutl {cipher_text}")

