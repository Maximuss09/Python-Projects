# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# for friend in friends:
#     print(friend)
#     print(friend + " pie")
#- ------------------------------------------------------------

# student_score = [50, 42, 85, 20, 71, 84, 49, 24, 59, 68, 99, 75, 65, 89, 86]

# total_exam = sum(student_score)
# print(total_exam)

# sume = 0
# for score in student_score:
#     sume += score
# print(sume)
# #print(max(student_score))

# max_score = 0

# for score in student_score:
#     if score > max_score:
#         max_score = score
# print(max_score)

# -------------------------------------------------------------
#       RANGE FUNCTION 

# for number in range(1, 21, 2):
#     print(number)

# total = 0
# for gauss in range(1, 101):
#     total += gauss

# print(total)
# ------------------------------------------------------------
#       QUIZ

#

for solution in range(1, 101):
    if solution % 3 == 0 and solution % 5 == 0:
        print("FrizzBuzz")
    elif solution % 3 == 0:
        print("Fizz")
    elif solution % 5 == 0:
        print("Buzz")
    else:
        print(solution)
