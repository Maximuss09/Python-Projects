logo = '''

                               _                                      __             
   ____ ___  _____  __________(_)___  ____ _   ____  __  ______ ___  / /_  ___  _____
  / __ `/ / / / _ \/ ___/ ___/ / __ \/ __ `/  / __ \/ / / / __ `__ \/ __ \/ _ \/ ___/
 / /_/ / /_/ /  __(__  |__  ) / / / / /_/ /  / / / / /_/ / / / / / / /_/ /  __/ /    
 \__, /\__,_/\___/____/____/_/_/ /_/\__, /  /_/ /_/\__,_/_/ /_/ /_/_.___/\___/_/     
/____/                             /____/                                            


'''
import random
print(logo)
print("Welcome to the Number guessing Game!")

print("I'm thinking of a number between 1 and 100")
thinking_number = random.randint(1, 100)
print(thinking_number)

def play_game(lives):
    game_not_finish = True
    
    while game_not_finish:
        print(f"You have {lives} attempts remaining to guess the number")
        guessing_number = int(input("Make a guess:  "))
        if guessing_number == thinking_number:
            print(f"You got it. The anwer was: {thinking_number}")
            game_not_finish = False

        elif guessing_number > thinking_number:
            print("Too High")
            lives -= 1
            if lives == 0:
                print("You've run out of guesses, you lose")
                game_not_finish = False
            else:
                print("Guess Again. ")

        elif guessing_number < thinking_number:
            print("Too Low.")
            lives -= 1
            if lives == 0:
                print("You've run out of guesses, you lose")
                game_not_finish = False
            else:
                print("Guess Again. ")


difficulty = (input("Choose a difficulty. Type 'easy' or 'hard':  ")).lower()


if difficulty == "easy":
    play_game(lives=10)

elif difficulty == "hard":
    play_game(lives=5)

else:
    print("ok")
