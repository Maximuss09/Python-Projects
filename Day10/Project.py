logo = '''
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ '.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ '.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   '._____.'  | || ||____|  |____|| || |  |________|  | || |   '._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|

'''

print(logo)


def add (n1, n2):
    return n1 + n2

def substract (a1, a2):
    return a1 - a2

def multiply (b1, b2):
    return b1 * b2

def divide (c1, c2):
    return c1 / c2

operation_dictionary = {
    "+" : add,
    "-" : substract,
    "*" : multiply,
    "/" : divide

}



def calculator():

    calculation_over = False
    x = float(input("Write the first number of the operation: "))

    while not calculation_over:
    
        print (" + \n - \n * \n /" )
        operation_to_do = str(input("Pick an operation from the list: "))
        if operation_to_do not in operation_dictionary:
          print("Sorry that's not a valid operation")
          calculation_over = True
          continue

        y = float(input("Write the second number of the operation: "))
        results = operation_dictionary[operation_to_do](x, y)

        print(f"Result: {x} {operation_to_do} {y} = {results}")

        continue_calculation = input(f"Type 'y' to continue calculation with {results} or type n to start a new calculation: ")
        if continue_calculation == "y":
            x = results
        else:
            calculation_over = True
            print("\n"*20)
            calculator()


calculator()



