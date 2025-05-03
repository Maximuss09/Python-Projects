# with open ("C:/Users/ttpin/OneDrive/Documentos/Python Docs/Day25_CSV&Pandas/weather_data.csv") as file:
#     list_data = file.readlines()
#     print (list_data)

# import csv

# with open ("Day25_CSV&Pandas\weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempeture = []
#     for modofacker in data:
#         # print(modofacker)
#         if modofacker[1] != "temp":
#             tempeture.append(int(modofacker[1]))
#     print(tempeture)

import pandas

data = pandas.read_csv("Day25_CSV&Pandas\weather_data.csv")
# print(type(data["temp"]))
# print(type(data))

dictionary = data.to_dict()
# print(dictionary)

temp_list = data["temp"].to_list()
# print(len(temp_list))

# avg_temp = sum(temp_list)/len(temp_list)
# print(avg_temp)

"---------Get Max and mean value----------"
# print(data["temp"].mean())
print(data["temp"].max())

"----------Get Data in Columns-----------"
# print(data["condition"])
# print(data.condition)

"----------Get Data in Row--------------"
# print(data[data.day =="Friday"])
print(data[data.temp == data.temp.max()])

monday = data[data.temp == "Monday"]

