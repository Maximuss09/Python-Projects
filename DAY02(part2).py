## PROJECT 

print("WELCOME TO THE CALCULATOR TIP")
bill = float(input("What was the total bill? $"))
tip = float(input("How much tip would you like to give? 10, 12, 15, 20? "))
split = int(input("How many people to split the bill? "))
payment = (bill + (bill*(tip/100)))/split
payment_rounded = round(payment, 2)
print(f"Each person should pay: {payment_rounded}")

