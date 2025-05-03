import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_not_finished = True

while game_not_finished:
    question = input("Do you want to play BlackJack? Type 'yes' or 'no': ").lower()
    
    if question == "yes":
        user_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards)]

        user_sum = sum(user_cards)
        computer_sum = sum(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {computer_cards[0]}")

        # Check if the player hits a Blackjack right away
        if user_sum == 21:
            print("Congratulations! You got a BlackJack")
            game_not_finished = False
            continue
        
        # Player's turn
        while user_sum < 21:
            other_card = input("Do you want to get another card? Type 'yes' or 'no': ").lower()
            if other_card == "yes":
                user_cards.append(random.choice(cards))
                user_sum = sum(user_cards)
                print(f"Your cards: {user_cards}, current score: {user_sum}")
            else:
                break
        
        # Check if player has busted
        if user_sum > 21:
            print("Sorry, you went over 21. You lose.")
            game_not_finished = False
            continue
        elif user_sum == 21:
            print("Congrats! You got 21!")
            game_not_finished = False
            continue
        
        # Dealer's turn
        while computer_sum < 17:
            computer_cards.append(random.choice(cards))
            computer_sum = sum(computer_cards)
        
        print(f"Your final hand: {user_cards}, final score: {user_sum}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_sum}")

        # Determine the winner
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
        game_not_finished = False
