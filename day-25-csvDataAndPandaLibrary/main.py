# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     # "_csv.reader
#     print(type(data))
#     # It iterates and prints every row, when I only need temperatures, I only want the row[1]
#     for row in data:
#         # Each row is a list
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# #     print(temperatures)
#
import pandas
#
# # It takes the first row to be the name of each column and it automatically knows how to find the data
# # The whole table is a DataFrame
# # And every single column is a Series, kinda like a list
# data =  pandas.read_csv("weather_data.csv")
# # print(type(data))
# # print(type(data["temp"]))
# # print(data)
# # print(data["temp"])
#
#all columns
# data_dict = data.to_dict()
# print(data_dict)
#the temp column
# # temp_list = data["temp"].tolist()
# # average_temp = sum(temp_list) / len(temp_list)
# # print(average_temp)
# print(data["temp"].mean())
#
# print(data["temp"].max())
#
# # Get Data in Columns
# # print(data["condition"])
# # print(data.condition)
#
# # Get Data in Row
# print(data[data.day == "Monday"])
#
# # Print the row of data wich had the highest temperature
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_F = monday_temp * 9/5 + 32
# print(monday_temp_F)
#
# # Create a DataFrame from scratch
# data_dict1 = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data1 = pandas.DataFrame(data_dict1)
# data1.to_csv("new_data.csv")
#
# print(data1)

# Read csv
data =  pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#Tranform in dictionary

data_gray = len(data[data["Primary Fur Color"] == "Gray"])
data_cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
data_black = len(data[data["Primary Fur Color"] == "Black"])

print(data_gray)
# Int
print(type(data_gray))
data_dict = {
    "Fur color": ["Gray","Cinnamon","Black"],
    "Count": [data_gray, data_cinnamon,data_black]
}

df = pandas.DataFrame(data_dict)
df.to_csv("total_squirrel_colors.csv")


