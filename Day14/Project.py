import random
from art import logo, vs
from game_data import data

print(logo)
score = 0
game_should_continue = True
account_a = random.choice(data)
account_b = random.choice(data)

def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    
    return f"{name}, a {description}, from {country}"


while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}")
    print(vs)
    print(f"Compare B: {format_data(account_b)}")

    guess = input("Who has more followers? Type A or B: ").lower()
    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    print(" \n"*20)
    print(logo)
    if a_followers_count > b_followers_count:
        correct_answer = 'a'
    else:
        correct_answer = 'b'

    if guess == correct_answer:
        score += 1
        print(f"You're right! Your score is {score}")
    else:
        game_should_continue = False
        print(f"Sorry that's wrong. Final score {score}")



