# number = [1, 2, 3]
# new_number = [new_item for item in list]      "EXPRESION"
# new_number = [n + 1 for n in number]
# print(new_number)

# range_list = [n*n for n in range(1,5)]
# print(range_list)

"""---------------------------------"""

# names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
#print(names)
#Short_names = [new_item for item in list if test]      "EXPRESION"
# short_names = [name for name in names if len(name)<5]
# print(short_names)

# capital_names = [name.upper() for name in names if len(name)>5]
# print(capital_names)

"""------------DICTIONARY COMPREHENSION---------------"""
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
# student_scores = {new_key:new_value for item in list}     "EXPRESION"
student_scores = {student:random.randint(50,100) for student in names}
# print(student_scores)
# passed_students = {new_key:new_value for (key, value) in dictionary.item()}  ""EXPRESION""
# passed_students = {student:score for (student, score) in student_scores.items() if score >= 70}
# print(passed_students)

"""-------------------Excercise----------------------"""
# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# result = {word:len(word ) for word in sentence.split()}
# print(result)


weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:((temp_c * 9/5) + 32) for (day, temp_c) in weather_c.items()}

print(weather_f)



