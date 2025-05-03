print ("WELCOME TO MY F*KING GAME")
print("Your mission is not to die while finding the treasure in a desertic Island")

answer1 = input("Do you know how to swim? Type yes or no: "). lower() 

if answer1 == "yes":
    answer2 = input('Ok you still alive. Now, a little bird told you that the treasure is in another island.'
          'Type "wait" to wait for a magical signal. '
          'Type "swim" to swim until you find the other island: '). lower()
    if answer2 == "swim":
        answer3 = input('Supresly, sharks does not eat you and the island was pretty close. '
                        'But now you realise there is a cave with 3 differents paths.'
                        'Which one do you choose? Type "left" or "middle" or "right": '). lower()
        if answer3 == "left":
            print("You been eating by rats, srry. GAME OVER ")
        elif answer3 == "middle":
            print("Your feet got stuck in on some rocks trying to pass them, srry GAME OVER")
        elif answer3 == "right":
            print ("You fall into a cannibals trap, srry. GAME OVER")
        else:
            print("That path doesn't exist. Game Over")

    else:
        print("There is no such thing as a magical signal. GAME OVER :)")
    
else:
    print ("Sorry you died x_x. GAME OVER")
