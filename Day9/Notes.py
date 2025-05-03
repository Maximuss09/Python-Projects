programming_dictionary = {
    "Bug": "An error in program that prevent the program from running as expected",
    "Function": "A piece of code that you can easily call over and over",
    "Loop": "The action of doing something over and over"
}

print(programming_dictionary["Bug"])

programming_dictionary["Bug"] = "Something new"  # EDIT AN ITEM ON A DICTIONARY
print(programming_dictionary)


for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


# ------------------------QUIZ----------------------------

# student_scores = {
#     'Harry': 88,
#     'Ron': 78,
#     'Hermione': 95,
#     'Draco': 75,
#     'Neville': 60
# }

# student_grades = {

# }


# for key in student_scores:

#     if student_scores[key] >= 91:
#         student_grades[key] = "Outstanding"
#     elif student_scores[key] >= 81:
#         student_grades[key] = "Exceeds Expectations"
#     elif student_scores[key] >=71:
#         student_grades[key] = "Acceptable"
#     elif student_scores[key] <= 70:
#         student_grades[key] = "Fail"

# print(student_grades)

#-------------------------------------------------------
        
# capitals = {
#     "France": "Paris",
#     "German": "Berlin"
# }

    # Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "German": ["Stuttgart", "Berlin"],
}

print(travel_log["France"][1])


nested_list = ["A", "B", ["C", "D"]]

print(nested_list[2][1])

#--------------------------------------------------------

# travel_log = {
#     "France": {
#         "citire_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12,
#         },

#     "German": {
#         "cities_visited": ["Stuttgart", "Hambur", "Berlin"],
#         "total_visits": 5
#         }
# }

# print(travel_log["German"]["cities_visited"][2])






