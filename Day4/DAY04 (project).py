import random
rock = '''

    _ _ _ _ 
---'  _ _ _ )
     (_ _ _ _)
     (_ _ _ _)
      (_ _ _)
 ---'_ (_ _)
    

'''

paper = '''
    _ _ _ _ 
---'    _ _ )_ _ _ _
              _ _ _ _)
               _ _ _ _)
                _ _ _)
 ---'_ _ _ _ _ _ _ _)

'''
scissors = '''
    _ _ _ _ 
---'    _ _ )_ _ _ _
              _ _ _ _)
            _ _ _ _ _)
       ( _ _ _)
 ---'_  ( _ _)
'''

options = [rock, paper, scissors]

choise = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER or 2 for SCISSORS: "))
decision = (random.choice(options))

if choise == 0:
    print(rock)
    print("Computer chose: ")
    print(decision)
    if decision == scissors:
        print("You Won. Impresive")
    elif decision == rock:
        print("That's a Tie")
    else:
        print("You Lose HAHA")

elif choise == 1:
    print(paper)
    print("Computer chose: ")
    print(decision)
    if decision == rock:
        print("You Won. Impresive")
    elif decision == paper:
        print("That's a Tie")
    else:
        print("You Lose HAHA")

elif choise == 2:
    print(scissors)
    print("Computer chose: ")
    print(decision)
    if decision == paper:
        print("You Won. Impresive")
    elif decision == scissors:
        print("That's a Tie")
    else:
        print("You Lose HAHA")
else:
    print("That's not an option.")