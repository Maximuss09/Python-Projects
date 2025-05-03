import random
import hangman
import hangman_words

print(hangman.logo)
word_list = hangman_words.words_to_guess
random_word = random.choice(word_list)
print(random_word)

stages = hangman.stages_of_lives

word_length = len(random_word)

place_holder = ""
for position in range(word_length):
    place_holder += "_"
print(place_holder)

game_over = False
correct_letters = []
live = 6

while game_over == False:

    guessed_letter = input("Guess a letter: ").lower()

    if guessed_letter in correct_letters:
        print(f"You already choose {guessed_letter}")

    disply = ""
    for letter in random_word:
        if letter == guessed_letter:
            disply += letter
            correct_letters.append(guessed_letter)
            print (f"You have {live} lives. Keep going")
        elif letter in correct_letters:
            disply += letter
        else:
            disply += "_"

    print(disply)

    if guessed_letter not in random_word:
        live -= 1
        print(f"You have {live} lives. That letter in not in the word")
        if live == 0:
            game_over = True
            print(f"The word was {random_word}")
            print("************You lose*************")


    if "_" not in disply:
        game_over = True
        print("***********You Win*************")

    print(stages[live])
