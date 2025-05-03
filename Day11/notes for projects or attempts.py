import random

logo = '''
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_|
      |  \/ K|                            _/ |                
      '------'                           |__/           
'''
print(logo)


# import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_not_finish = True

user_cards = []
computer_cards = []

while game_not_finish:
    question = str(input("Do you want to play BlackJack? Type 'yes' or 'no': ")).lower() 
    if question == "yes":
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))

        user_sum = sum(user_cards)
 

        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {computer_cards}")

        if user_sum == 21:
            print("Congratulations! You got a BlackJack")
            game_not_finish = False
            continue


        while user_sum <21:
            other_card = str(input("Do you want to get another card? Type 'yes' or 'no': ")).lower() #Tercera carta
        
            if other_card == "yes":
                user_cards.append(random.choice(cards))
                user_sum = sum(user_cards) 
                print(f"Your cards {user_cards}, current score: {user_sum}")
                print(f"Computer's card: {computer_cards}")
            else:
                break

        if user_sum > 21:
            print("Sorry, you went over 21. You lose.")
            game_not_finished = False
            continue
               
        elif user_sum == 21:
            print("Congrats! You got 21!")
            game_not_finished = False
            continue


        while computer_sum < 17:
            computer_cards.append(random.choice(cards))
            computer_sum = sum(computer_cards)
        
        print(f"Your final hand: {user_cards}, final score: {user_sum}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")

        if computer_sum > 21:
            print("Computer went over 21. You win!")
        elif computer_sum > user_sum:
            print("You lose!")
        elif user_sum > computer_sum:
            print("You win!")
        else:
            print("It's a tie!")
            
        game_not_finished = False

    else:
        game_not_finish = False



